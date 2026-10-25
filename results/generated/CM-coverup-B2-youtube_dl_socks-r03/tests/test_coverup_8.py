# file: project/youtube_dl/socks.py:138-141
# asked: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}
# gained: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}

import pytest

from youtube_dl.socks import InvalidVersionError, sockssocket


def _make_socket(monkeypatch):
    """Create a real sockssocket and record close() calls without leaking the fd."""
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
        monkeypatch.undo()
        sock.close()

    # postconditions: socket was closed exactly once, error describes both versions
    assert closed == [True]
    err = excinfo.value
    assert isinstance(err, InvalidVersionError)
    assert err.args[0] == 0
    assert "Expected 05" in str(err)
    assert "got 04" in str(err)


def test_check_response_version_mismatch_closes_before_raising(monkeypatch):
    sock, closed = _make_socket(monkeypatch)
    try:
        with pytest.raises(InvalidVersionError):
            sock._check_response_version(0x00, 0x05)
        # close() must have happened before the exception propagated
        assert closed == [True]
    finally:
        monkeypatch.undo()
        sock.close()


def test_check_response_version_match_does_not_close(monkeypatch):
    sock, closed = _make_socket(monkeypatch)
    try:
        assert sock._check_response_version(0x05, 0x05) is None
        assert closed == []
    finally:
        monkeypatch.undo()
        sock.close()
