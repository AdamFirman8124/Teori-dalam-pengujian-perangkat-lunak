# file: project/youtube_dl/socks.py:138-141
# asked: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}
# gained: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}

import socket

import pytest

from youtube_dl.socks import InvalidVersionError, sockssocket


@pytest.fixture
def sock():
    s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    yield s
    s.close()


def test_check_response_version_matching_does_not_close(sock):
    sock._check_response_version(5, 5)
    assert sock.fileno() != -1


def test_check_response_version_mismatch_closes_and_raises(sock):
    with pytest.raises(InvalidVersionError) as excinfo:
        sock._check_response_version(5, 4)

    assert sock.fileno() == -1
    assert excinfo.value.args[0] == 0
    assert 'Expected 05 got 04' in excinfo.value.args[1]


def test_check_response_version_mismatch_closes_socket(monkeypatch):
    s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    closed = []
    monkeypatch.setattr(s, 'close', lambda: closed.append(True))

    with pytest.raises(InvalidVersionError):
        s._check_response_version(4, 5)

    assert closed == [True]
    s.close()
