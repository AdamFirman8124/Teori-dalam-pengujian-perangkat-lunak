# file: project/youtube_dl/socks.py:58-64
# asked: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}

from youtube_dl.socks import ProxyError


def test_proxy_error_uses_message_for_known_code(monkeypatch):
    monkeypatch.setattr(ProxyError, "CODES", {7: "mapped error"}, raising=False)

    error = ProxyError(7)

    assert error.args == (7, "mapped error")


def test_proxy_error_uses_unknown_message_for_unmapped_code(monkeypatch):
    monkeypatch.setattr(ProxyError, "CODES", {}, raising=False)

    error = ProxyError(99)

    assert error.args == (99, "unknown error")


def test_proxy_error_preserves_explicit_message():
    error = ProxyError(7, "explicit error")

    assert error.args == (7, "explicit error")


def test_proxy_error_accepts_no_arguments():
    error = ProxyError()

    assert error.args == (None, None)
