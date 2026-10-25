# file: project/youtube_dl/socks.py:112-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

import socket

from youtube_dl.socks import sockssocket


def test_sockssocket_init_sets_proxy_none():
    s = sockssocket()
    try:
        assert s._proxy is None
        assert isinstance(s, socket.socket)
    finally:
        s.close()


def test_sockssocket_init_with_args_kwargs():
    s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        assert s._proxy is None
        assert s.family == socket.AF_INET
        assert s.type == socket.SOCK_STREAM
    finally:
        s.close()
