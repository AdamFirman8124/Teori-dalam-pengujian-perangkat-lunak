# file: project/youtube_dl/socks.py:121-128
# asked: {"lines": [122, 123, 124, 125, 126, 127, 128], "branches": [[123, 124], [123, 128], [125, 126], [125, 127]]}
# gained: {"lines": [122, 123, 124, 125, 126, 127, 128], "branches": [[123, 124], [123, 128], [125, 126], [125, 127]]}

import pytest

from youtube_dl.socks import sockssocket


def test_recvall_collects_multiple_chunks(monkeypatch):
    chunks = [b'ab', b'cde']
    requested_sizes = []

    def fake_recv(self, size):
        requested_sizes.append(size)
        return chunks.pop(0)

    monkeypatch.setattr(sockssocket, 'recv', fake_recv)

    sock = sockssocket()
    with sock:
        assert sock.recvall(5) == b'abcde'
        assert requested_sizes == [5, 3]
        assert chunks == []

    assert sock.fileno() == -1


def test_recvall_raises_eoferror_for_incomplete_data(monkeypatch):
    chunks = [b'ab', b'']
    requested_sizes = []

    def fake_recv(self, size):
        requested_sizes.append(size)
        return chunks.pop(0)

    monkeypatch.setattr(sockssocket, 'recv', fake_recv)

    sock = sockssocket()
    with sock:
        with pytest.raises(EOFError) as exc_info:
            sock.recvall(5)

        assert str(exc_info.value) == '3 bytes missing'
        assert requested_sizes == [5, 3]
        assert chunks == []

    assert sock.fileno() == -1
