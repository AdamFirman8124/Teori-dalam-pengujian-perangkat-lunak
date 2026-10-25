# file: project/youtube_dl/socks.py:58-64
# asked: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}

from youtube_dl.socks import ProxyError


def test_proxy_error_uses_message_for_known_code():
    class TestProxyError(ProxyError):
        CODES = {1: "known error"}

    error = TestProxyError(1)

    assert error.args == (1, "known error")
    assert error.errno == 1
    assert error.strerror == "known error"


def test_proxy_error_uses_fallback_message_for_unknown_code():
    class TestProxyError(ProxyError):
        CODES = {}

    error = TestProxyError(99)

    assert error.args == (99, "unknown error")
    assert error.errno == 99
    assert error.strerror == "unknown error"


def test_proxy_error_preserves_explicit_message():
    class TestProxyError(ProxyError):
        CODES = {1: "mapped message"}

    error = TestProxyError(1, "explicit message")

    assert error.args == (1, "explicit message")
    assert error.errno == 1
    assert error.strerror == "explicit message"


def test_proxy_error_accepts_no_code_or_message():
    class TestProxyError(ProxyError):
        CODES = {}

    error = TestProxyError()

    assert error.args == (None, None)
    assert error.errno is None
    assert error.strerror is None
