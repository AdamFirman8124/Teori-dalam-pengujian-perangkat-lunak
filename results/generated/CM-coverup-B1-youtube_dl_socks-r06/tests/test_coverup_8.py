# file: project/youtube_dl/socks.py:67-71
# asked: {"lines": [69, 70, 71], "branches": []}
# gained: {"lines": [69, 70, 71], "branches": []}

from youtube_dl.socks import InvalidVersionError, ProxyError


def test_invalid_version_error_formats_versions_and_sets_proxy_error_details():
    expected_version = 0x05
    got_version = 0x0A
    expected_message = (
        'Invalid response version from server. Expected 05 got 0a'
    )

    error = InvalidVersionError(expected_version, got_version)

    assert isinstance(error, ProxyError)
    assert error.args == (0, expected_message)
    assert error.errno == 0
    assert error.strerror == expected_message
    assert str(error) == '[Errno 0] %s' % expected_message
