# file: project/youtube_dl/socks.py:269-270
# asked: {"lines": [270], "branches": []}
# gained: {"lines": [270], "branches": []}

import socket

import pytest

from youtube_dl import socks as socks_module
from youtube_dl.socks import sockssocket


@pytest.fixture
def sock():
    s = sockssocket()
    try:
        yield s
    finally:
        s.close()


def test_connect_calls_make_proxy_with_socket_connect(sock, monkeypatch):
    calls = []

    def fake_make_proxy(self, connect_func, address):
        calls.append((self, connect_func, address))
        return 'ignored'

    monkeypatch.setattr(sockssocket, '_make_proxy', fake_make_proxy)

    address = ('127.0.0.1', 8080)
    result = sock.connect(address)

    assert result is None
    assert calls == [(sock, socket.socket.connect, address)]


def test_connect_without_proxy_delegates_to_socket_connect(sock, monkeypatch):
    calls = []

    def fake_connect(self, address):
        calls.append((self, address))
        return 0

    monkeypatch.setattr(socket.socket, 'connect', fake_connect)

    address = ('example.com', 443)
    result = sock.connect(address)

    assert result is None
    assert calls == [(sock, address)]


def test_connect_with_proxy_connects_to_proxy_and_runs_setup(sock, monkeypatch):
    proxy_type = getattr(getattr(socks_module, 'ProxyType', None), 'SOCKS5', None)
    if proxy_type is None:
        pytest.skip('ProxyType.SOCKS5 is not available')

    sock.setproxy(proxy_type, 'proxy.example.com', 1080)

    connect_calls = []
    setup_calls = []

    def fake_connect(self, address):
        connect_calls.append((self, address))
        return 0

    def fake_setup(self, address):
        setup_calls.append((self, address))

    monkeypatch.setattr(socket.socket, 'connect', fake_connect)
    monkeypatch.setattr(sockssocket, '_setup_socks5', fake_setup)

    address = ('target.example.com', 80)
    result = sock.connect(address)

    assert result is None
    assert connect_calls == [(sock, ('proxy.example.com', 1080))]
    assert setup_calls == [(sock, address)]


def test_connect_with_proxy_skips_setup_when_proxy_connect_fails(sock, monkeypatch):
    proxy_type = getattr(getattr(socks_module, 'ProxyType', None), 'SOCKS5', None)
    if proxy_type is None:
        pytest.skip('ProxyType.SOCKS5 is not available')

    sock.setproxy(proxy_type, 'proxy.example.com', 1080)

    connect_calls = []
    setup_calls = []

    def fake_connect(self, address):
        connect_calls.append((self, address))
        return 1

    def fake_setup(self, address):
        setup_calls.append((self, address))

    monkeypatch.setattr(socket.socket, 'connect', fake_connect)
    monkeypatch.setattr(sockssocket, '_setup_socks5', fake_setup)

    address = ('target.example.com', 80)
    result = sock.connect(address)

    assert result is None
    assert connect_calls == [(sock, ('proxy.example.com', 1080))]
    assert setup_calls == []
