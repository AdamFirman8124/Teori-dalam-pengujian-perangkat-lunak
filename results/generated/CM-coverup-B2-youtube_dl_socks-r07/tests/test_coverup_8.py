# file: project/youtube_dl/socks.py:138-141
# asked: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}
# gained: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}

import socket

import pytest

from youtube_dl.socks import InvalidVersionError, sockssocket


def test_check_response_version_mismatch_closes_and_raises(monkeypatch):
    s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        close_calls = []
        orig_close = socket.socket.close

        def fake_close(*args, **kwargs):
            close_calls.append(1)
            return orig_close(s)

        monkeypatch.setattr(s, "close", fake_close)

        with pytest.raises(InvalidVersionError) as exc_info:
            s._check_response_version(0x05, 0x04)

        # postconditions: close() was called exactly once
        assert close_calls == [1]
        # postconditions: correct error code and message
        expected_msg = "Invalid response version from server. Expected 05 got 04"
        assert exc_info.value.args == (0, expected_msg)
        assert exc_info.value.args[0] == 0
        assert expected_msg in str(exc_info.value)
        # postconditions: underlying socket is closed
        assert s.fileno() == -1
    finally:
        try:
            socket.socket.close(s)
        except Exception:
            pass


def test_check_response_version_match_does_not_close_or_raise(monkeypatch):
    s = sockssocket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        def fail_close(*args, **kwargs):
            pytest.fail("close() should not be called on version match")

        monkeypatch.setattr(s, "close", fail_close)

        assert s._check_response_version(0x05, 0x05) is None
        # postconditions: socket still open
        assert s.fileno() != -1
    finally:
        # bypass monkeypatched close to guarantee cleanup
        try:
            socket.socket.close(s)
        except Exception:
            pass
