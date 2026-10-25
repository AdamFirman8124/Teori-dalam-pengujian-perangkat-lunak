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


def test_make_proxy_no_proxy(sock, monkeypatch):
    """Lines 255-256: without a proxy, connect_func is called directly."""
    address = ('example.com', 80)
    sentinel = object()
    calls = []

    def fake_connect(s, addr):
        calls.append((s, addr))
        return sentinel

    result = sock._make_proxy(fake_connect, address)

    assert result is sentinel
    assert calls == [(sock, address)]
    assert sock._proxy is None


def _make_proxy_sock(sock, proxytype):
    sock.setproxy(proxytype, '127.0.0.1', 1080, rdns=True,
                  username='user', password='pass')
    return sock


@pytest.mark.parametrize('proxytype,setup_name', [
    (ProxyType.SOCKS4, '_setup_socks4'),
    (ProxyType.SOCKS4A, '_setup_socks4a'),
    (ProxyType.SOCKS5, '_setup_socks5'),
])
def test_make_proxy_success_dispatches_setup(sock, monkeypatch, proxytype, setup_name):
    """Lines 258, 261-267: successful connect dispatches to the right setup func."""
    _make_proxy_sock(sock, proxytype)
    address = ('example.com', 80)
    setup_calls = []

    def fake_setup(addr):
        setup_calls.append(addr)
        return None

    monkeypatch.setattr(sock, setup_name, fake_setup)

    def fake_connect(s, addr):
        assert (s, addr) == (sock, ('127.0.0.1', 1080))
        return 0

    result = sock._make_proxy(fake_connect, address)

    assert result == 0
    assert setup_calls == [address]


def test_make_proxy_connect_error_returned(sock, monkeypatch):
    """Lines 258-260: nonzero connect result is returned early, no setup run."""
    _make_proxy_sock(sock, ProxyType.SOCKS5)
    address = ('example.com', 80)
    setup_called = []

    def fake_setup(addr):
        setup_called.append(addr)

    monkeypatch.setattr(sock, '_setup_socks5', fake_setup)

    def fake_connect(s, addr):
        return 10061  # e.g. connection refused error code

    result = sock._make_proxy(fake_connect, address)

    assert result == 10061
    assert setup_called == []


def test_make_proxy_connect_returns_none(sock, monkeypatch):
    """Line 259 branch: None result is not treated as an error; setup runs and None is returned."""
    _make_proxy_sock(sock, ProxyType.SOCKS4)
    address = ('example.com', 80)
    setup_calls = []

    def fake_setup(addr):
        setup_calls.append(addr)

    monkeypatch.setattr(sock, '_setup_socks4', fake_setup)

    def fake_connect(s, addr):
        return None

    result = sock._make_proxy(fake_connect, address)

    assert result is None
    assert setup_calls == [address]
