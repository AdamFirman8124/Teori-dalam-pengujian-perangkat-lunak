# file: project/youtube_dl/socks.py:58-64
# asked: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}

from youtube_dl.socks import Socks5Error


def test_proxy_error_uses_message_for_known_code():
    error = Socks5Error(Socks5Error.ERR_GENERAL_FAILURE)

    assert error.args == (
        Socks5Error.ERR_GENERAL_FAILURE,
        "general SOCKS server failure",
    )


def test_proxy_error_uses_unknown_message_for_unrecognized_code():
    error = Socks5Error(12345)

    assert error.args == (12345, "unknown error")


def test_proxy_error_preserves_explicit_message():
    error = Socks5Error(Socks5Error.ERR_GENERAL_FAILURE, "custom message")

    assert error.args == (Socks5Error.ERR_GENERAL_FAILURE, "custom message")


def test_proxy_error_accepts_no_code_or_message():
    error = Socks5Error()

    assert error.args == (None, None)
