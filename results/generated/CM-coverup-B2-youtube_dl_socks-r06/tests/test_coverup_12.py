# file: project/youtube_dl/socks.py:130-132
# asked: {"lines": [131, 132], "branches": []}
# gained: {"lines": [131, 132], "branches": []}

import pytest

from youtube_dl.socks import sockssocket


@pytest.fixture
def mock_sockssocket(monkeypatch):
    """Create a sockssocket instance without opening a real socket,
    and stub out recv/recvall so no network I/O occurs."""
    sock = sockssocket.__new__(sockssocket)

    def fake_recvall(self, cnt):
        # Simulate data arriving in two chunks to exercise the loop in recvall
        return bytes(range(cnt % 256))[:cnt]

    monkeypatch.setattr(sockssocket, 'recvall', fake_recvall)
    return sock


def test_recv_bytes_unpacks_data(mock_sockssocket):
    cnt = 4
    result = mock_sockssocket._recv_bytes(cnt)
    # Postcondition: returns a tuple of cnt unsigned ints (network byte order)
    assert isinstance(result, tuple)
    assert len(result) == cnt
    assert result == (0, 1, 2, 3)
    assert all(isinstance(b, int) and 0 <= b <= 255 for b in result)


def test_recv_bytes_single_byte(mock_sockssocket):
    result = mock_sockssocket._recv_bytes(1)
    assert result == (0,)
