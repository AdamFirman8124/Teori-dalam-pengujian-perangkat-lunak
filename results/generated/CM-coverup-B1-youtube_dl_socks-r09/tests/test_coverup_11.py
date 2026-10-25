# file: project/youtube_dl/socks.py:130-132
# asked: {"lines": [131, 132], "branches": []}
# gained: {"lines": [131, 132], "branches": []}

from youtube_dl.socks import sockssocket


def test_recv_bytes_single_byte(monkeypatch):
    sock = sockssocket.__new__(sockssocket)
    monkeypatch.setattr(sock, "recvall", lambda cnt: b"\x05")
    result = sock._recv_bytes(1)
    assert result == (5,)


def test_recv_bytes_multiple_bytes_verifies_cnt(monkeypatch):
    sock = sockssocket.__new__(sockssocket)
    seen = {}

    def fake_recvall(cnt):
        seen["cnt"] = cnt
        return b"\x01\x02\xff"

    monkeypatch.setattr(sock, "recvall", fake_recvall)
    result = sock._recv_bytes(3)
    assert seen["cnt"] == 3
    assert result == (1, 2, 255)
    assert isinstance(result, tuple)
    assert len(result) == 3
