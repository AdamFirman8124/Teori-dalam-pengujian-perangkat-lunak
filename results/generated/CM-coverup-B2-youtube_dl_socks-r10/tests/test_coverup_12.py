# file: project/youtube_dl/socks.py:130-132
# asked: {"lines": [131, 132], "branches": []}
# gained: {"lines": [131, 132], "branches": []}

import socket

import pytest

from youtube_dl.socks import sockssocket


@pytest.fixture
def sock():
    s = sockssocket()
    try:
        yield s
    finally:
        s.close()


def test_recv_bytes_unpacks_single_byte(sock, monkeypatch):
    calls = []

    def fake_recvall(self, cnt):
        calls.append(cnt)
        return b'\x05'

    monkeypatch.setattr(sockssocket, 'recvall', fake_recvall)

    result = sock._recv_bytes(1)

    assert result == (5,)
    assert isinstance(result, tuple)
    assert calls == [1]


def test_recv_bytes_unpacks_multiple_bytes(sock, monkeypatch):
    calls = []

    def fake_recvall(self, cnt):
        calls.append(cnt)
        return bytes(range(cnt))

    monkeypatch.setattr(sockssocket, 'recvall', fake_recvall)

    result = sock._recv_bytes(3)

    assert result == (0, 1, 2)
    assert calls == [3]


def test_recv_bytes_uses_network_byte_order(sock, monkeypatch):
    monkeypatch.setattr(sockssocket, 'recvall', lambda self, cnt: b'\x00\xff')

    result = sock._recv_bytes(2)

    # '!2B' is big-endian unsigned bytes: 0x00 -> 0, 0xff -> 255
    assert result == (0, 255)


def test_recv_bytes_propagates_recvall_error(sock, monkeypatch):
    def failing_recvall(self, cnt):
        raise socket.timeout('timed out')

    monkeypatch.setattr(sockssocket, 'recvall', failing_recvall)

    with pytest.raises(socket.timeout):
        sock._recv_bytes(4)
