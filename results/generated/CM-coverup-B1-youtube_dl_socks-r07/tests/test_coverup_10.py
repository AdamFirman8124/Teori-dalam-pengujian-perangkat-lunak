# file: project/youtube_dl/socks.py:112-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

import socket

from youtube_dl.socks import sockssocket


def test_sockssocket_initialization():
    sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        assert isinstance(sock, socket.socket)
        assert sock._proxy is None
        assert sock.family == socket.AF_INET
        assert sock.type == socket.SOCK_STREAM
        assert sock.fileno() >= 0
    finally:
        sock.close()

    assert sock.fileno() == -1
