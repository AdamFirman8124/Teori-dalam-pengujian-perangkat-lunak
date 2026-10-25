# file: project/youtube_dl/socks.py:121-128
# asked: {"lines": [122, 123, 124, 125, 126, 127, 128], "branches": [[123, 124], [123, 128], [125, 126], [125, 127]]}
# gained: {"lines": [122, 123, 124, 125, 126, 127, 128], "branches": [[123, 124], [123, 128], [125, 126], [125, 127]]}

import pytest

from youtube_dl.socks import sockssocket


def test_recvall_collects_multiple_chunks(monkeypatch):
    chunks = iter((b'ab', b'cde'))
    requested_sizes = []

    def fake_recv(self, size):
        requested_sizes.append(size)
        return next(chunks)

    monkeypatch.setattr(sockssocket, 'recv', fake_recv)

    sock = sockssocket()
    try:
        assert sock.recvall(5) == b'abcde'
        assert requested_sizes == [5, 3]
    finally:
        sock.close()


def test_recvall_raises_eoferror_when_connection_closes_early(monkeypatch):
    chunks = iter((b'ab', b''))
    requested_sizes = []

    def fake_recv(self, size):
        requested_sizes.append(size)
        return next(chunks)

    monkeypatch.setattr(sockssocket, 'recv', fake_recv)

    sock = sockssocket()
    try:
        with pytest.raises(EOFError, match=r'^3 bytes missing$'):
            sock.recvall(5)
        assert requested_sizes == [5, 3]
    finally:
        sock.close()


def test_recvall_returns_empty_bytes_for_zero_count(monkeypatch):
    def unexpected_recv(self, size):
        pytest.fail('recv must not be called when the requested count is zero')

    monkeypatch.setattr(sockssocket, 'recv', unexpected_recv)

    sock = sockssocket()
    try:
        assert sock.recvall(0) == b''
    finally:
        sock.close()
