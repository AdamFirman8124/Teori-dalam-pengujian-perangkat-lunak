# file: project/youtube_dl/socks.py:58-64
# asked: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}

import socket

import pytest

from youtube_dl.socks import ProxyError, Socks5Error


@pytest.mark.parametrize(
    ("code", "expected_message"),
    [
        (Socks5Error.ERR_GENERAL_FAILURE, "general SOCKS server failure"),
        (0x100, "unknown error"),
    ],
)
def test_proxy_error_derives_message_from_code(code, expected_message):
    error = Socks5Error(code)

    assert isinstance(error, ProxyError)
    assert isinstance(error, socket.error)
    assert error.args == (code, expected_message)


def test_proxy_error_preserves_explicit_message():
    error = Socks5Error(Socks5Error.ERR_GENERAL_FAILURE, "custom message")

    assert error.args == (Socks5Error.ERR_GENERAL_FAILURE, "custom message")


def test_proxy_error_accepts_no_code_or_message():
    error = Socks5Error()

    assert error.args == (None, None)
