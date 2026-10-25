# file: project/youtube_dl/socks.py:67-71
# asked: {"lines": [69, 70, 71], "branches": []}
# gained: {"lines": [69, 70, 71], "branches": []}

import pytest

from youtube_dl.socks import InvalidVersionError, ProxyError


@pytest.mark.parametrize(
    ("expected_version", "got_version"),
    [
        (0x05, 0x04),
        (0x01, 0x00),
    ],
)
def test_invalid_version_error_message_and_arguments(
    expected_version, got_version
):
    error = InvalidVersionError(expected_version, got_version)
    expected_message = (
        "Invalid response version from server. Expected {0:02x} got {1:02x}"
    ).format(expected_version, got_version)

    assert isinstance(error, ProxyError)
    assert error.args == (0, expected_message)
