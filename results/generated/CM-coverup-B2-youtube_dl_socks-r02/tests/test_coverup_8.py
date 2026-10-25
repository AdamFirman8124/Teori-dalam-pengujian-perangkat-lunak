# file: project/youtube_dl/socks.py:138-141
# asked: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}
# gained: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}

import socket

import pytest

from youtube_dl.socks import InvalidVersionError, sockssocket


def test_check_response_version_mismatch_closes_socket_and_raises(monkeypatch):
    sock = sockssocket()
    real_close = socket.socket.close
    close_calls = []

    def fake_close(self):
        close_calls.append(self)

    monkeypatch.setattr(sockssocket, 'close', fake_close)
    try:
        with pytest.raises(InvalidVersionError) as excinfo:
            sock._check_response_version(0x05, 0x04)

        # close() must have been called exactly once, on this socket
        assert close_calls == [sock]

        # the error must carry the expected/got versions in its message
        message = str(excinfo.value)
        assert '05' in message
        assert '04' in message
    finally:
        # really release the underlying file descriptor
        real_close(sock)


def test_check_response_version_match_does_not_close_or_raise(monkeypatch):
    sock = sockssocket()
    real_close = socket.socket.close
    close_calls = []

    def fake_close(self):
        close_calls.append(self)

    monkeypatch.setattr(sockssocket, 'close', fake_close)
    try:
        assert sock._check_response_version(0x05, 0x05) is None
        assert close_calls == []
    finally:
        real_close(sock)
