# file: project/youtube_dl/socks.py:112-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

import socket

import pytest

from youtube_dl.socks import sockssocket


@pytest.fixture
def created_sockets():
    """Track sockets created by tests so they are always closed."""
    sockets = []
    yield sockets
    for sock in sockets:
        try:
            sock.close()
        except OSError:
            pass


def test_sockssocket_init_sets_proxy_and_calls_super(created_sockets):
    sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    created_sockets.append(sock)

    # __init__ must initialize _proxy to None before delegating to socket.socket
    assert sock._proxy is None
    # super().__init__ must have run: real socket state is initialized
    assert isinstance(sock, socket.socket)
    assert sock.family == socket.AF_INET
    assert sock.type == socket.SOCK_STREAM
    assert sock.fileno() != -1


def test_sockssocket_init_forwards_args_and_kwargs(created_sockets):
    sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    created_sockets.append(sock)

    assert sock._proxy is None
    assert sock.proto == 0
    assert sock.fileno() != -1


def test_sockssocket_init_accepts_no_args(created_sockets):
    sock = sockssocket()
    created_sockets.append(sock)

    assert sock._proxy is None
    assert isinstance(sock, socket.socket)
    assert sock.fileno() != -1
