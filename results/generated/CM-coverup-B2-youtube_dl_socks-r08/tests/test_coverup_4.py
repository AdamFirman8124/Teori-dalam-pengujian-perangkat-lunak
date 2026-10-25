# file: project/youtube_dl/socks.py:254-267
# asked: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}
# gained: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}

import pytest

from youtube_dl.socks import Proxy, ProxyType, sockssocket


@pytest.fixture
def sock():
    s = sockssocket()
    yield s
    try:
        s.close()
    except OSError:
        pass


def _install_fake_setups(monkeypatch, sock):
    calls = []
    monkeypatch.setattr(sock, "_setup_socks4", lambda address: calls.append(("socks4", address)))
    monkeypatch.setattr(sock, "_setup_socks4a", lambda address: calls.append(("socks4a", address)))
    monkeypatch.setattr(sock, "_setup_socks5", lambda address: calls.append(("socks5", address)))
    return calls


def _set_proxy(sock, proxy_type):
    sock._proxy = Proxy(
        type=proxy_type,
        host="127.0.0.1",
        port=1080,
        username=None,
        password=None,
        remote_dns=True,
    )


def test_make_proxy_no_proxy_direct_connect(sock, monkeypatch):
    setup_calls = _install_fake_setups(monkeypatch, sock)
    assert sock._proxy is None
    connect_calls = []

    def connect_func(self_arg, address):
        connect_calls.append((self_arg, address))
        return 42

    result = sock._make_proxy(connect_func, ("example.com", 80))

    assert result == 42
    assert connect_calls == [(sock, ("example.com", 80))]
    assert setup_calls == []


def test_make_proxy_connect_error_returns_without_setup(sock, monkeypatch):
    _set_proxy(sock, ProxyType.SOCKS5)
    setup_calls = _install_fake_setups(monkeypatch, sock)
    connect_calls = []

    def connect_func(self_arg, address):
        connect_calls.append((self_arg, address))
        return 111

    result = sock._make_proxy(connect_func, ("example.com", 443))

    assert result == 111
    assert connect_calls == [(sock, ("127.0.0.1", 1080))]
    assert setup_calls == []


@pytest.mark.parametrize(
    "proxy_type,setup_name",
    [
        (ProxyType.SOCKS4, "socks4"),
        (ProxyType.SOCKS4A, "socks4a"),
        (ProxyType.SOCKS5, "socks5"),
    ],
)
@pytest.mark.parametrize("connect_result", [0, None])
def test_make_proxy_dispatches_to_correct_setup(sock, monkeypatch, proxy_type, setup_name, connect_result):
    _set_proxy(sock, proxy_type)
    setup_calls = _install_fake_setups(monkeypatch, sock)
    connect_calls = []

    def connect_func(self_arg, address):
        connect_calls.append((self_arg, address))
        return connect_result

    result = sock._make_proxy(connect_func, ("example.com", 80))

    assert result is connect_result or result == connect_result
    assert connect_calls == [(sock, ("127.0.0.1", 1080))]
    assert setup_calls == [(setup_name, ("example.com", 80))]
