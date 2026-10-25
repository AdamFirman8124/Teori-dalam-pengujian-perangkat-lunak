# file: project/youtube_dl/socks.py:269-270
# asked: {"lines": [270], "branches": []}
# gained: {"lines": [270], "branches": []}

import socket

from youtube_dl.socks import sockssocket


def test_connect_delegates_to_make_proxy(monkeypatch):
    calls = []

    def fake_make_proxy(self, connect_func, address):
        calls.append((self, connect_func, address))

    monkeypatch.setattr(sockssocket, "_make_proxy", fake_make_proxy)

    address = ("example.com", 443)
    proxy_socket = sockssocket()
    try:
        result = proxy_socket.connect(address)

        assert result is None
        assert calls == [(proxy_socket, socket.socket.connect, address)]
    finally:
        proxy_socket.close()
