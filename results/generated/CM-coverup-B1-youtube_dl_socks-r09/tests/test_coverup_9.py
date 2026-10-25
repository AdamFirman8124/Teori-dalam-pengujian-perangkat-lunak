# file: project/youtube_dl/socks.py:67-71
# asked: {"lines": [69, 70, 71], "branches": []}
# gained: {"lines": [69, 70, 71], "branches": []}

from youtube_dl.socks import InvalidVersionError, ProxyError


def test_invalid_version_error_message_and_attributes():
    error = InvalidVersionError(0x05, 0x04)

    expected_message = (
        "Invalid response version from server. Expected 05 got 04"
    )
    assert isinstance(error, ProxyError)
    assert error.args == (0, expected_message)
    assert error.errno == 0
    assert error.strerror == expected_message
