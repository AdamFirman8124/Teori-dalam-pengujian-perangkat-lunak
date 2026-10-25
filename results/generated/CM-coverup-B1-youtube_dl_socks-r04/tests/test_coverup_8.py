# file: project/youtube_dl/socks.py:138-141
# asked: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}
# gained: {"lines": [139, 140, 141], "branches": [[139, 0], [139, 140]]}

import pytest

from youtube_dl.socks import InvalidVersionError, sockssocket


def test_check_response_version_mismatch_closes_and_raises(monkeypatch):
    sock = sockssocket()
    closed = []
    monkeypatch.setattr(sock, 'close', lambda: closed.append(True))
    try:
        with pytest.raises(InvalidVersionError) as exc_info:
            sock._check_response_version(0x05, 0x04)
    finally:
        monkeypatch.undo()
        try:
            sock.close()
        except OSError:
            pass

    assert closed == [True]
    assert exc_info.value.args == (
        0,
        'Invalid response version from server. Expected 05 got 04',
    )


def test_check_response_version_match_does_not_close_or_raise(monkeypatch):
    sock = sockssocket()
    closed = []
    monkeypatch.setattr(sock, 'close', lambda: closed.append(True))
    try:
        sock._check_response_version(0x05, 0x05)
    finally:
        monkeypatch.undo()
        try:
            sock.close()
        except OSError:
            pass

    assert closed == []
