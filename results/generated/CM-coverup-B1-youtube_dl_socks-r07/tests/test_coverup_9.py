# file: project/youtube_dl/socks.py:67-71
# asked: {"lines": [69, 70, 71], "branches": []}
# gained: {"lines": [69, 70, 71], "branches": []}

import pytest

from youtube_dl.socks import InvalidVersionError, ProxyError


def test_invalid_version_error_message_formatting():
    exc = InvalidVersionError(0x05, 0x04)

    assert isinstance(exc, ProxyError)
    assert exc.args[0] == 0
    assert exc.args[1] == 'Invalid response version from server. Expected 05 got 04'


def test_invalid_version_error_zero_padded_hex():
    exc = InvalidVersionError(0x00, 0x0A)

    assert exc.args[1] == 'Invalid response version from server. Expected 00 got 0a'


def test_invalid_version_error_is_raisable_and_catchable():
    with pytest.raises(InvalidVersionError) as excinfo:
        raise InvalidVersionError(0x05, 0x01)

    err = excinfo.value
    assert err.args == (0, 'Invalid response version from server. Expected 05 got 01')
    assert isinstance(err, ProxyError)
