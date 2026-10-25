# file: project/youtube_dl/socks.py:138-141
# asked: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}
# gained: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}

import pytest

from youtube_dl.socks import sockssocket, InvalidVersionError


def test_check_response_version_mismatch_closes_and_raises(monkeypatch):
    closed = []

    def fake_close():
        closed.append(True)

    sock = sockssocket()
    try:
        monkeypatch.setattr(sock, 'close', fake_close)

        with pytest.raises(InvalidVersionError) as exc_info:
            sock._check_response_version(0x05, 0x00)

        # close() was called before raising
        assert closed == [True]

        # The exception carries the expected and got versions
        assert exc_info.value.args == (0, 'Invalid response version from server. Expected 05 got 00')
    finally:
        # Ensure no real socket leaks even if assertions fail
        try:
            real_close = socket_socket_close = sockssocket.close.__wrapped__ if hasattr(
                sockssocket.close, '__wrapped__') else None
        except Exception:
            real_close = None
        if not closed:
            # close() was never invoked; close the underlying socket directly
            import socket as _socket
            try:
                _socket.socket.close(sock)
            except OSError:
                pass


def test_check_response_version_match_does_not_raise(monkeypatch):
    closed = []

    def fake_close():
        closed.append(True)

    sock = sockssocket()
    try:
        monkeypatch.setattr(sock, 'close', fake_close)

        # Matching versions must not raise and must not close the socket
        result = sock._check_response_version(0x05, 0x05)

        assert result is None
        assert closed == []
    finally:
        import socket as _socket
        try:
            _socket.socket.close(sock)
        except OSError:
            pass
