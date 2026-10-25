# file: project/youtube_dl/socks.py:67-71
# asked: {"lines": [69, 70, 71], "branches": []}
# gained: {"lines": [69, 70, 71], "branches": []}

from youtube_dl.socks import InvalidVersionError, ProxyError


def test_invalid_version_error_message():
    exc = InvalidVersionError(0x05, 0x00)
    expected_msg = 'Invalid response version from server. Expected 05 got 00'
    assert isinstance(exc, ProxyError)
    assert exc.args[0] == 0
    assert exc.args[1] == expected_msg
    assert expected_msg in str(exc)


def test_invalid_version_error_raise_and_format():
    expected_version = 0x05
    got_version = 0xFF
    expected_msg = 'Invalid response version from server. Expected 05 got ff'
    try:
        raise InvalidVersionError(expected_version, got_version)
    except ProxyError as e:
        assert e.args == (0, expected_msg)
        assert expected_msg in str(e)
        assert '{0:02x}'.format(expected_version) in str(e)
        assert '{0:02x}'.format(got_version) in str(e)
    else:
        assert False, 'InvalidVersionError was not raised'
