# file: project/youtube_dl/socks.py:272-273
# asked: {"lines": [273], "branches": []}
# gained: {"lines": [273], "branches": []}

import socket

import pytest

from youtube_dl.socks import ProxyType, sockssocket


@pytest.fixture
def sock():
    s = sockssocket()
    yield s
    s.close()


def test_connect_ex_without_proxy(sock, monkeypatch):
    """connect_ex (line 273) with no proxy set must delegate directly to
    socket.socket.connect_ex and return its result."""
    sentinel = 12345
    calls = []

    def fake_connect_ex(self, address):
        calls.append(address)
        return sentinel

    monkeypatch.setattr(socket.socket, 'connect_ex', fake_connect_ex)

    address = ('example.com', 80)
    result = sock.connect_ex(address)

    assert result == sentinel
    assert calls == [address]


def test_connect_ex_with_proxy_success(sock, monkeypatch):
    """connect_ex with a proxy must connect to the proxy address, run the
    SOCKS setup for the original destination, and return 0."""
    proxy_addr = ('proxy.example.com', 1080)
    dest_addr = ('dest.example.com', 80)
    connect_calls = []
    setup_calls = []

    def fake_connect_ex(self, address):
        connect_calls.append(address)
        return 0

    def fake_setup_socks5(self, address):
        setup_calls.append(address)

    monkeypatch.setattr(socket.socket, 'connect_ex', fake_connect_ex)
    monkeypatch.setattr(sockssocket, '_setup_socks5', fake_setup_socks5)

    sock.setproxy(ProxyType.SOCKS5, proxy_addr[0], proxy_addr[1])
    result = sock.connect_ex(dest_addr)

    assert result == 0
    assert connect_calls == [proxy_addr]
    assert setup_calls == [dest_addr]


def test_connect_ex_with_proxy_connect_failure(sock, monkeypatch):
    """If connecting to the proxy itself fails (nonzero result), the SOCKS
    setup must not run and the error code must be returned."""
    proxy_addr = ('proxy.example.com', 1080)
    dest_addr = ('dest.example.com', 80)
    error_code = 111
    connect_calls = []
    setup_calls = []

    def fake_connect_ex(self, address):
        connect_calls.append(address)
        return error_code

    def fake_setup_socks5(self, address):
        setup_calls.append(address)

    monkeypatch.setattr(socket.socket, 'connect_ex', fake_connect_ex)
    monkeypatch.setattr(sockssocket, '_setup_socks5', fake_setup_socks5)

    sock.setproxy(ProxyType.SOCKS5, proxy_addr[0], proxy_addr[1])
    result = sock.connect_ex(dest_addr)

    assert result == error_code
    assert connect_calls == [proxy_addr]
    assert setup_calls == []
