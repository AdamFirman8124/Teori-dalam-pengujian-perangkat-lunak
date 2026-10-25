# file: project/youtube_dl/socks.py:269-270
# asked: {"lines": [270], "branches": []}
# gained: {"lines": [270], "branches": []}

import socket

from youtube_dl import socks


def test_sockssocket_connect_delegates_to_make_proxy(monkeypatch):
    calls = []

    def fake_make_proxy(self, connect_func, address):
        calls.append((self, connect_func, address))

    monkeypatch.setattr(socks.sockssocket, "_make_proxy", fake_make_proxy)

    address = ("example.com", 443)
    with socks.sockssocket() as sock:
        result = sock.connect(address)

        assert result is None
        assert calls == [(sock, socket.socket.connect, address)]
