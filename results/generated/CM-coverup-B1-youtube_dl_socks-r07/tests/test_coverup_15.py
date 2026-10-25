# file: project/youtube_dl/socks.py:269-270
# asked: {"lines": [270], "branches": []}
# gained: {"lines": [270], "branches": []}

import socket

from youtube_dl.socks import sockssocket


def test_connect_delegates_to_make_proxy(monkeypatch):
    calls = []

    def fake_make_proxy(self, connect_func, address):
        calls.append((self, connect_func, address))
        return object()

    monkeypatch.setattr(sockssocket, "_make_proxy", fake_make_proxy)

    sock = sockssocket()
    address = ("example.com", 443)
    try:
        result = sock.connect(address)
    finally:
        sock.close()

    assert result is None
    assert len(calls) == 1
    assert calls[0][0] is sock
    assert calls[0][1] is socket.socket.connect
    assert calls[0][2] == address
    assert sock.fileno() == -1
