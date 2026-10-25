# file: project/youtube_dl/socks.py:112-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

import socket

from youtube_dl.socks import sockssocket


def test_sockssocket_init_default():
    s = sockssocket()
    try:
        assert s._proxy is None
        assert isinstance(s, socket.socket)
        assert s.family in (socket.AF_INET, socket.AF_INET6)
        assert s.type == socket.SOCK_STREAM
    finally:
        s.close()


def test_sockssocket_init_with_positional_args():
    s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        assert s._proxy is None
        assert isinstance(s, socket.socket)
        assert s.family == socket.AF_INET
        assert s.type == socket.SOCK_STREAM
    finally:
        s.close()


def test_sockssocket_init_with_kwargs():
    s = sockssocket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    try:
        assert s._proxy is None
        assert isinstance(s, socket.socket)
        assert s.family == socket.AF_INET
        assert s.type == socket.SOCK_STREAM
    finally:
        s.close()
