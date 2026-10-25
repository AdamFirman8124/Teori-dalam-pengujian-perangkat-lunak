# file: project/youtube_dl/socks.py:58-64
# asked: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}

import socket

from youtube_dl.socks import ProxyError


def test_proxy_error_uses_message_for_known_code(monkeypatch):
    monkeypatch.setattr(ProxyError, "CODES", {1: "known error"}, raising=False)

    error = ProxyError(1)

    assert isinstance(error, socket.error)
    assert error.args == (1, "known error")


def test_proxy_error_uses_fallback_for_unknown_code(monkeypatch):
    monkeypatch.setattr(ProxyError, "CODES", {}, raising=False)

    error = ProxyError(999)

    assert error.args == (999, "unknown error")


def test_proxy_error_preserves_explicit_message_without_codes():
    error = ProxyError(1, "custom error")

    assert error.args == (1, "custom error")


def test_proxy_error_accepts_no_arguments():
    error = ProxyError()

    assert error.args == (None, None)
