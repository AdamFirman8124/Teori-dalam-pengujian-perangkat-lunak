# file: project/youtube_dl/socks.py:138-141
# asked: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}
# gained: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}

import socket

import pytest

from youtube_dl.socks import InvalidVersionError, sockssocket


def _make_socket():
    return sockssocket(socket.AF_INET, socket.SOCK_STREAM)


@pytest.mark.parametrize('expected, got', [
    (0x05, 0x04),
    (0x04, 0x00),
    (0x05, 0xff),
])
def test_check_response_version_mismatch_closes_then_raises(monkeypatch, expected, got):
    s = _make_socket()
    real_close = s.close
    calls = []

    def fake_close():
        calls.append('close')
        real_close()

    monkeypatch.setattr(s, 'close', fake_close)
    try:
        with pytest.raises(InvalidVersionError) as excinfo:
            s._check_response_version(expected, got)

        # close() must have been called exactly once, before the raise
        assert calls == ['close']
        # the underlying socket really is closed
        assert s.fileno() == -1

        err = excinfo.value
        assert isinstance(err, socket.error)
        assert err.args == (
            0,
            'Invalid response version from server. Expected {0:02x} got {1:02x}'.format(
                expected, got),
        )
    finally:
        real_close()


def test_check_response_version_mismatch_does_not_raise_on_match(monkeypatch):
    s = _make_socket()
    closed = []
    monkeypatch.setattr(s, 'close', lambda: closed.append(True))
    try:
        assert s._check_response_version(0x05, 0x05) is None
        assert closed == []
        # socket was left open
        assert s.fileno() != -1
    finally:
        socket.socket.close(s)
