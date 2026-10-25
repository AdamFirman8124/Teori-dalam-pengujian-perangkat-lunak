# file: project/youtube_dl/socks.py:121-128
# asked: {"lines": [122, 123, 124, 125, 126, 127, 128], "branches": [[123, 124], [123, 128], [125, 126], [125, 127]]}
# gained: {"lines": [122, 123, 124, 125, 126, 127, 128], "branches": [[123, 124], [123, 128], [125, 126], [125, 127]]}

import pytest

from youtube_dl.socks import sockssocket


def _make_socket(recv_results):
    """Create a sockssocket without opening a real socket, with a stubbed recv."""
    sock = sockssocket.__new__(sockssocket)
    calls = []

    def fake_recv(cnt):
        calls.append(cnt)
        result = recv_results.pop(0)
        if isinstance(result, Exception):
            raise result
        return result

    sock.recv = fake_recv
    return sock, calls


def test_recvall_single_recv():
    sock, calls = _make_socket([b'hello'])
    assert sock.recvall(5) == b'hello'
    assert calls == [5]


def test_recvall_multiple_recvs():
    sock, calls = _make_socket([b'ab', b'cd', b'e'])
    assert sock.recvall(5) == b'abcde'
    assert calls == [5, 3, 1]


def test_recvall_more_data_than_requested():
    sock, calls = _make_socket([b'abcdef'])
    assert sock.recvall(3) == b'abcdef'
    assert calls == [3]


def test_recvall_zero_bytes():
    sock, calls = _make_socket([])
    assert sock.recvall(0) == b''
    assert calls == []


def test_recvall_eof_raises():
    sock, calls = _make_socket([b'ab', b''])
    with pytest.raises(EOFError) as excinfo:
        sock.recvall(5)
    assert str(excinfo.value) == '3 bytes missing'
    assert calls == [5, 3]


def test_recvall_eof_on_first_recv():
    sock, calls = _make_socket([b''])
    with pytest.raises(EOFError) as excinfo:
        sock.recvall(4)
    assert str(excinfo.value) == '4 bytes missing'
    assert calls == [4]
