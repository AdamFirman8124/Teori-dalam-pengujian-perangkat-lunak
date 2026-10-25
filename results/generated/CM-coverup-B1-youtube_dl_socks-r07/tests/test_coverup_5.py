# file: project/youtube_dl/socks.py:121-128
# asked: {"lines": [122, 123, 124, 125, 126, 127, 128], "branches": [[123, 124], [123, 128], [125, 126], [125, 127]]}
# gained: {"lines": [122, 123, 124, 125, 126, 127, 128], "branches": [[123, 124], [123, 128], [125, 126], [125, 127]]}

import pytest

from youtube_dl.socks import sockssocket


def _make_scripted_socket(chunks):
    class ScriptedSocket(sockssocket):
        def __init__(self):
            super().__init__()
            self.recv_sizes = []
            self._chunks = iter(chunks)

        def recv(self, size, flags=0):
            self.recv_sizes.append(size)
            return next(self._chunks)

    return ScriptedSocket()


def test_recvall_accumulates_partial_reads():
    sock = _make_scripted_socket([b'ab', b'cde'])

    with sock:
        assert sock.recvall(5) == b'abcde'
        assert sock.recv_sizes == [5, 3]

    assert sock.fileno() == -1


def test_recvall_raises_eoferror_when_peer_closes_early():
    sock = _make_scripted_socket([b'ab', b''])

    with sock:
        with pytest.raises(EOFError, match=r'^3 bytes missing$'):
            sock.recvall(5)
        assert sock.recv_sizes == [5, 3]

    assert sock.fileno() == -1
