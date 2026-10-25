# file: project/youtube_dl/socks.py:112-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

import socket

import pytest

from youtube_dl.socks import sockssocket


def test_sockssocket_init_covers_proxy_and_super_init():
    sock = sockssocket()
    try:
        # Lines 113-114: _proxy is initialized and super().__init__ runs.
        assert sock._proxy is None
        # Verify the underlying socket was properly initialized by super().
        assert isinstance(sock, socket.socket)
        assert sock.fileno() != -1
    finally:
        # Clean up to avoid leaking file descriptors / state pollution.
        sock.close()


def test_sockssocket_init_with_args_forwarded_to_super():
    # Exercise __init__ with arguments forwarded to socket.socket's __init__.
    sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        assert sock._proxy is None
        assert sock.type == socket.SOCK_STREAM
        assert sock.family == socket.AF_INET
    finally:
        sock.close()
