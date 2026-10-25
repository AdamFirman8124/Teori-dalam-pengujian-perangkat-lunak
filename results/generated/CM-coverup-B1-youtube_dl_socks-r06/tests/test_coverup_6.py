# file: project/youtube_dl/socks.py:58-64
# asked: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [62, 63, 64], "branches": [[62, 63], [62, 64]]}

import pytest

from youtube_dl.socks import ProxyError


@pytest.mark.parametrize(
    ("code", "message", "codes", "expected_args"),
    [
        (7, None, {7: "mapped error"}, (7, "mapped error")),
        (8, None, {}, (8, "unknown error")),
        (9, "explicit error", {9: "mapped error"}, (9, "explicit error")),
        (None, None, {}, (None, None)),
    ],
)
def test_proxy_error_initialization(
    monkeypatch, code, message, codes, expected_args
):
    monkeypatch.setattr(ProxyError, "CODES", codes, raising=False)

    error = ProxyError(code, message)

    assert error.args == expected_args
