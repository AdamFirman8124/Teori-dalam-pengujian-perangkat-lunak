# file: project/youtube_dl/socks.py:254-267
# asked: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}
# gained: {"lines": [255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267], "branches": [[255, 256], [255, 258], [259, 260], [259, 261]]}

import pytest

from youtube_dl.socks import Proxy, ProxyType, sockssocket


@pytest.fixture
def socks_socket():
    sock = sockssocket()
    try:
        yield sock
    finally:
        sock.close()


def test_make_proxy_without_configured_proxy(socks_socket):
    address = ("destination.example", 443)
    calls = []

    def connect_func(sock, connected_address):
        calls.append((sock, connected_address))
        return 17

    result = socks_socket._make_proxy(connect_func, address)

    assert result == 17
    assert calls == [(socks_socket, address)]
    assert socks_socket._proxy is None


def test_make_proxy_returns_nonzero_connection_error_without_setup(
        socks_socket, monkeypatch):
    setup_calls = []

    def unexpected_setup(sock, address):
        setup_calls.append((sock, address))

    monkeypatch.setattr(sockssocket, "_setup_socks4", unexpected_setup)
    monkeypatch.setattr(sockssocket, "_setup_socks4a", unexpected_setup)
    monkeypatch.setattr(sockssocket, "_setup_socks5", unexpected_setup)

    socks_socket._proxy = Proxy(
        ProxyType.SOCKS5, "proxy.example", 1080, None, None, True)
    connect_calls = []

    def connect_func(sock, address):
        connect_calls.append((sock, address))
        return 111

    result = socks_socket._make_proxy(
        connect_func, ("destination.example", 443))

    assert result == 111
    assert connect_calls == [(socks_socket, ("proxy.example", 1080))]
    assert setup_calls == []


@pytest.mark.parametrize(
    ("proxy_type", "expected_setup", "connect_result"),
    [
        (ProxyType.SOCKS4, "socks4", 0),
        (ProxyType.SOCKS4A, "socks4a", None),
        (ProxyType.SOCKS5, "socks5", 0),
    ],
)
def test_make_proxy_dispatches_setup_after_successful_connection(
        socks_socket, monkeypatch, proxy_type, expected_setup, connect_result):
    setup_calls = []

    def setup_socks4(sock, address):
        setup_calls.append(("socks4", sock, address))

    def setup_socks4a(sock, address):
        setup_calls.append(("socks4a", sock, address))

    def setup_socks5(sock, address):
        setup_calls.append(("socks5", sock, address))

    monkeypatch.setattr(sockssocket, "_setup_socks4", setup_socks4)
    monkeypatch.setattr(sockssocket, "_setup_socks4a", setup_socks4a)
    monkeypatch.setattr(sockssocket, "_setup_socks5", setup_socks5)

    socks_socket._proxy = Proxy(
        proxy_type, "proxy.example", 1080, "user", "password", True)
    destination = ("destination.example", 443)
    connect_calls = []

    def connect_func(sock, address):
        connect_calls.append((sock, address))
        return connect_result

    result = socks_socket._make_proxy(connect_func, destination)

    assert result is connect_result
    assert connect_calls == [(socks_socket, ("proxy.example", 1080))]
    assert setup_calls == [(expected_setup, socks_socket, destination)]
