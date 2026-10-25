# file: project/youtube_dl/socks.py:112-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

import socket

import pytest

from youtube_dl.socks import sockssocket


@pytest.fixture
def created_sockets():
    sockets = []
    yield sockets
    for s in sockets:
        try:
            s.close()
        except OSError:
            pass


def test_sockssocket_init_sets_proxy_and_initializes_socket(created_sockets):
    sock = sockssocket()
    created_sockets.append(sock)

    assert sock._proxy is None
    assert isinstance(sock, socket.socket)
    assert sock.fileno() != -1


def test_sockssocket_init_forwards_args_to_socket(created_sockets):
    sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    created_sockets.append(sock)

    assert sock._proxy is None
    assert sock.family == socket.AF_INET
    assert sock.type == socket.SOCK_STREAM
    assert sock.fileno() != -1


def test_sockssocket_init_forwards_kwargs_to_socket(created_sockets):
    sock = sockssocket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    created_sockets.append(sock)

    assert sock._proxy is None
    assert sock.family == socket.AF_INET
    assert sock.type == socket.SOCK_STREAM
    assert sock.fileno() != -1


def test_sockssocket_init_proxy_is_per_instance(created_sockets):
    first = sockssocket()
    second = sockssocket()
    created_sockets.extend([first, second])

    first._proxy = ("socks5", "127.0.0.1", 1080)

    assert second._proxy is None
    assert first._proxy == ("socks5", "127.0.0.1", 1080)
