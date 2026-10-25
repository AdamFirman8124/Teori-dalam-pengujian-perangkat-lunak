# file: project/youtube_dl/socks.py:112-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

import socket

import pytest

from youtube_dl.socks import sockssocket


def test_sockssocket_init_sets_proxy_none():
    sock = sockssocket()
    try:
        assert sock._proxy is None
        assert isinstance(sock, socket.socket)
    finally:
        sock.close()


def test_sockssocket_init_with_args():
    # __init__ must forward args/kwargs to socket.socket
    sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        assert sock._proxy is None
        assert sock.family == socket.AF_INET
        assert sock.type == socket.SOCK_STREAM
    finally:
        sock.close()
