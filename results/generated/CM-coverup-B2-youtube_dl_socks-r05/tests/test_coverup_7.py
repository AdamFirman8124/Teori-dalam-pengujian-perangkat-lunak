# file: project/youtube_dl/socks.py:58-64
# asked: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}

import pytest

from youtube_dl.socks import ProxyError


def test_proxy_error_uses_message_for_known_code(monkeypatch):
    monkeypatch.setattr(ProxyError, "CODES", {7: "known error"}, raising=False)

    error = ProxyError(7)

    assert error.args == (7, "known error")
    assert error.errno == 7
    assert error.strerror == "known error"


def test_proxy_error_uses_fallback_message_for_unknown_code(monkeypatch):
    monkeypatch.setattr(ProxyError, "CODES", {}, raising=False)

    error = ProxyError(99)

    assert error.args == (99, "unknown error")
    assert error.errno == 99
    assert error.strerror == "unknown error"


@pytest.mark.parametrize(
    ("code", "message"),
    [
        (None, None),
        (7, "explicit message"),
    ],
)
def test_proxy_error_does_not_look_up_message_when_condition_is_false(
    monkeypatch, code, message
):
    class FailingCodes:
        def get(self, key):
            pytest.fail("CODES.get() must not be called")

    monkeypatch.setattr(ProxyError, "CODES", FailingCodes(), raising=False)

    error = ProxyError(code, message)

    assert error.args == (code, message)
    assert error.errno == code
    assert error.strerror == message
