# file: project/youtube_dl/socks.py:121-128
# asked: {"lines": [122, 123, 124, 125, 126, 127, 128], "branches": [[123, 124], [123, 128], [125, 126], [125, 127]]}
# gained: {"lines": [122, 123, 124, 125, 126, 127, 128], "branches": [[123, 124], [123, 128], [125, 126], [125, 127]]}

import pytest

from youtube_dl.socks import sockssocket


def test_recvall_collects_multiple_chunks():
    class ScriptedSocket(sockssocket):
        def __init__(self):
            super().__init__()
            self.chunks = iter((b"ab", b"cde"))
            self.recv_sizes = []

        def recv(self, size, *args):
            self.recv_sizes.append(size)
            return next(self.chunks)

    with ScriptedSocket() as sock:
        assert sock.recvall(5) == b"abcde"
        assert sock.recv_sizes == [5, 3]


def test_recvall_raises_eoferror_for_incomplete_data():
    class ScriptedSocket(sockssocket):
        def __init__(self):
            super().__init__()
            self.chunks = iter((b"ab", b""))

        def recv(self, size, *args):
            return next(self.chunks)

    with ScriptedSocket() as sock:
        with pytest.raises(EOFError, match=r"^3 bytes missing$"):
            sock.recvall(5)


def test_recvall_returns_immediately_for_zero_bytes():
    class NoRecvSocket(sockssocket):
        def recv(self, size, *args):
            pytest.fail("recv must not be called when zero bytes are requested")

    with NoRecvSocket() as sock:
        assert sock.recvall(0) == b""
