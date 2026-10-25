# file: project/youtube_dl/socks.py:138-141
# asked: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}
# gained: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}

import socket

import pytest

from youtube_dl.socks import InvalidVersionError, sockssocket


def test_check_response_version_mismatch_closes_and_raises(monkeypatch):
    s = sockssocket()
    try:
        close_calls = []
        monkeypatch.setattr(s, "close", lambda *a, **k: close_calls.append(True))
        with pytest.raises(InvalidVersionError) as excinfo:
            s._check_response_version(0x05, 0x04)
        # postconditions: close() was called exactly once before raising
        assert close_calls == [True]
        # postconditions: exception message reports expected vs got versions
        msg = str(excinfo.value)
        assert "05" in msg
        assert "04" in msg
        assert "Invalid response version" in msg
    finally:
        # clean up real socket fd bypassing the monkeypatched close
        try:
            socket.socket.close(s)
        except Exception:
            pass


def test_check_response_version_match_does_not_close_or_raise(monkeypatch):
    s = sockssocket()
    try:
        close_calls = []
        monkeypatch.setattr(s, "close", lambda *a, **k: close_calls.append(True))
        assert s._check_response_version(0x05, 0x05) is None
        assert close_calls == []
    finally:
        try:
            socket.socket.close(s)
        except Exception:
            pass
