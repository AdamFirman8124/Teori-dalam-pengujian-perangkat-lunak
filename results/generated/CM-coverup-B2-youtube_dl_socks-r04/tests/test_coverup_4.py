# file: project/youtube_dl/socks.py:254-267
# asked: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}
# gained: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}

import socket

import pytest

from youtube_dl.socks import ProxyType, sockssocket


@pytest.fixture
def sock():
    s = sockssocket()
    yield s
    s.close()


def make_connect_func(return_value):
    calls = []

    def connect_func(s, address):
        calls.append((s, address))
        return return_value

    connect_func.calls = calls
    return connect_func


def test_make_proxy_no_proxy_uses_connect_func_directly(sock, monkeypatch):
    address = ('example.com', 80)
    connect_func = make_connect_func(0)

    # Guard: if a proxy were set, the setup funcs would be called; ensure none are.
    for name in ('_setup_socks4', '_setup_socks4a', '_setup_socks5'):
        monkeypatch.setattr(
            sock, name,
            lambda *a, **kw: pytest.fail('setup func must not be called without a proxy'))

    result = sock._make_proxy(connect_func, address)

    assert result == 0
    assert connect_func.calls == [(sock, address)]


@pytest.mark.parametrize('proxytype,setup_name', [
    (ProxyType.SOCKS4, '_setup_socks4'),
    (ProxyType.SOCKS4A, '_setup_socks4a'),
    (ProxyType.SOCKS5, '_setup_socks5'),
])
def test_make_proxy_with_proxy_success(sock, monkeypatch, proxytype, setup_name):
    proxy_addr = ('proxy.example.com', 1080)
    dest_addr = ('dest.example.com', 80)
    sock.setproxy(proxytype, proxy_addr[0], proxy_addr[1])

    connect_func = make_connect_func(0)
    setup_calls = []

    def fake_setup(address):
        setup_calls.append(address)
        return ('fake', 1234)

    monkeypatch.setattr(sock, setup_name, fake_setup)
    # The other setup funcs must not be invoked.
    for name in ('_setup_socks4', '_setup_socks4a', '_setup_socks5'):
        if name != setup_name:
            monkeypatch.setattr(
                sock, name,
                lambda *a, **kw: pytest.fail('wrong setup func called: %s' % name))

    result = sock._make_proxy(connect_func, dest_addr)

    # connect_func must be called with the proxy address, not the destination.
    assert connect_func.calls == [(sock, proxy_addr)]
    # The correct setup func must be called with the destination address.
    assert setup_calls == [dest_addr]
    # The (successful) connect result is returned.
    assert result == 0


@pytest.mark.parametrize('return_value', [None, 0])
def test_make_proxy_falsy_result_proceeds_to_setup(sock, monkeypatch, return_value):
    sock.setproxy(ProxyType.SOCKS5, 'proxy.example.com', 1080)
    dest_addr = ('dest.example.com', 80)
    connect_func = make_connect_func(return_value)
    setup_calls = []
    monkeypatch.setattr(sock, '_setup_socks5', lambda address: setup_calls.append(address))

    result = sock._make_proxy(connect_func, dest_addr)

    assert setup_calls == [dest_addr]
    assert result is return_value


@pytest.mark.parametrize('return_value', [1, -1, 10061])
def test_make_proxy_nonzero_result_returns_early(sock, monkeypatch, return_value):
    sock.setproxy(ProxyType.SOCKS4, 'proxy.example.com', 1080)
    dest_addr = ('dest.example.com', 80)
    connect_func = make_connect_func(return_value)

    for name in ('_setup_socks4', '_setup_socks4a', '_setup_socks5'):
        monkeypatch.setattr(
            sock, name,
            lambda *a, **kw: pytest.fail('setup func must not be called on connect error'))

    result = sock._make_proxy(connect_func, dest_addr)

    assert result == return_value
    assert connect_func.calls == [(sock, ('proxy.example.com', 1080))]


def test_make_proxy_setup_func_exception_propagates(sock, monkeypatch):
    sock.setproxy(ProxyType.SOCKS5, 'proxy.example.com', 1080)
    connect_func = make_connect_func(0)

    class Boom(Exception):
        pass

    def failing_setup(address):
        raise Boom('setup failed')

    monkeypatch.setattr(sock, '_setup_socks5', failing_setup)

    with pytest.raises(Boom):
        sock._make_proxy(connect_func, ('dest.example.com', 80))
