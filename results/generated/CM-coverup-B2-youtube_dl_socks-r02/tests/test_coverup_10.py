# file: project/youtube_dl/socks.py:112-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

import socket

import pytest

from youtube_dl.socks import sockssocket


def test_sockssocket_init_sets_proxy_and_creates_socket():
    sock = sockssocket()
    try:
        assert sock._proxy is None
        assert isinstance(sock, socket.socket)
        assert sock.family == socket.AF_INET
        assert sock.type == socket.SOCK_STREAM
    finally:
        sock.close()


def test_sockssocket_init_passes_args_to_socket():
    sock = sockssocket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        assert sock._proxy is None
        assert sock.family == socket.AF_INET
        assert sock.type == socket.SOCK_DGRAM
    finally:
        sock.close()


def test_sockssocket_init_passes_kwargs_to_socket():
    sock = sockssocket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    try:
        assert sock._proxy is None
        assert sock.family == socket.AF_INET
        assert sock.type == socket.SOCK_STREAM
    finally:
        sock.close()


def test_sockssocket_init_calls_super_init(monkeypatch):
    calls = []
    real_init = socket.socket.__init__

    def fake_init(self, *args, **kwargs):
        calls.append((args, kwargs))
        real_init(self, *args, **kwargs)

    monkeypatch.setattr(socket.socket, '__init__', fake_init)

    sock = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        assert sock._proxy is None
        assert calls == [((socket.AF_INET, socket.SOCK_STREAM), {})]
    finally:
        sock.close()
