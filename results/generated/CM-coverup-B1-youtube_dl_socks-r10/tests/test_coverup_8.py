# file: project/youtube_dl/socks.py:138-141
# asked: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}
# gained: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}

import socket

import pytest

from youtube_dl.socks import InvalidVersionError, sockssocket


def test_check_response_version_mismatch_closes_and_raises(monkeypatch):
    sock = sockssocket()
    real_close = socket.socket.close.__get__(sock, sockssocket)
    close_calls = []

    def fake_close():
        close_calls.append(True)
        real_close()

    monkeypatch.setattr(sock, "close", fake_close)
    try:
        with pytest.raises(InvalidVersionError) as excinfo:
            sock._check_response_version(0x05, 0x04)

        assert close_calls == [True]
        expected_msg = "Invalid response version from server. Expected 05 got 04"
        assert excinfo.value.args == (0, expected_msg)
        assert expected_msg in str(excinfo.value)
        assert sock.fileno() == -1
    finally:
        try:
            real_close()
        except OSError:
            pass


def test_check_response_version_match_does_not_close_or_raise(monkeypatch):
    sock = sockssocket()
    close_calls = []
    monkeypatch.setattr(sock, "close", lambda: close_calls.append(True))
    try:
        result = sock._check_response_version(0x05, 0x05)

        assert result is None
        assert close_calls == []
        assert sock.fileno() != -1
    finally:
        socket.socket.close(sock)
