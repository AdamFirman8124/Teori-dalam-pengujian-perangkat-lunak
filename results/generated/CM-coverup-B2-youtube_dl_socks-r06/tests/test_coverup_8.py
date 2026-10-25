# file: project/youtube_dl/socks.py:138-141
# asked: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}
# gained: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}

import socket

import pytest

from youtube_dl.socks import InvalidVersionError, sockssocket


def _make_socket(monkeypatch):
    sock = sockssocket()
    closed = []
    monkeypatch.setattr(sock, "close", lambda: closed.append(True))
    return sock, closed


def test_check_response_version_mismatch_closes_and_raises(monkeypatch):
    sock, closed = _make_socket(monkeypatch)
    try:
        with pytest.raises(InvalidVersionError) as excinfo:
            sock._check_response_version(0x05, 0x04)
    finally:
        socket.socket.close(sock)

    assert closed == [True]
    err = excinfo.value
    assert err.errno == 0
    assert err.args[0] == 0
    assert "Expected 05" in str(err.args[1])
    assert "got 04" in str(err.args[1])


def test_check_response_version_mismatch_other_values(monkeypatch):
    sock, closed = _make_socket(monkeypatch)
    try:
        with pytest.raises(InvalidVersionError):
            sock._check_response_version(0x00, 0x05)
        assert closed == [True]
    finally:
        socket.socket.close(sock)


def test_check_response_version_match_does_not_close(monkeypatch):
    sock, closed = _make_socket(monkeypatch)
    try:
        assert sock._check_response_version(0x05, 0x05) is None
        assert closed == []
    finally:
        socket.socket.close(sock)
