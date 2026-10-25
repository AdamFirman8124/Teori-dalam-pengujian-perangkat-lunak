# file: project/youtube_dl/socks.py:67-71
# asked: {"lines": [69, 70, 71], "branches": []}
# gained: {"lines": [69, 70, 71], "branches": []}

from youtube_dl.socks import InvalidVersionError, ProxyError


def test_invalid_version_error():
    error = InvalidVersionError(0x05, 0x04)

    assert isinstance(error, ProxyError)
    assert error.args == (
        0,
        "Invalid response version from server. Expected 05 got 04",
    )
