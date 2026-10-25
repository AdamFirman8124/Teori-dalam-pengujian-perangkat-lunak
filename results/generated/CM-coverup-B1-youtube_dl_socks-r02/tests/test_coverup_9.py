# file: project/youtube_dl/socks.py:67-71
# asked: {"lines": [69, 70, 71], "branches": []}
# gained: {"lines": [69, 70, 71], "branches": []}

import pytest

from youtube_dl.socks import InvalidVersionError, ProxyError


def test_invalid_version_error_formats_message_and_initializes_proxy_error():
    expected_version = 0x05
    got_version = 0x0A
    expected_message = (
        "Invalid response version from server. Expected 05 got 0a"
    )

    with pytest.raises(InvalidVersionError) as exc_info:
        raise InvalidVersionError(expected_version, got_version)

    error = exc_info.value

    assert isinstance(error, ProxyError)
    assert error.args == (0, expected_message)
    assert str(error) == "[Errno 0] {}".format(expected_message)
