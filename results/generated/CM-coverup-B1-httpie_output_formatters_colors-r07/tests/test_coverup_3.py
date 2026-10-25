# file: project/httpie/output/formatters/colors.py:81-89
# asked: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}

import pytest

from httpie.output.formatters import colors
from httpie.output.formatters.colors import ColorFormatter


def test_format_body_highlights_when_lexer_is_available(monkeypatch):
    color_formatter = object.__new__(ColorFormatter)
    lexer = object()
    formatter = object()
    color_formatter.formatter = formatter

    monkeypatch.setattr(
        color_formatter,
        "get_lexer_for_body",
        lambda mime, body: lexer,
    )

    calls = []

    def fake_highlight(*, code, lexer, formatter):
        calls.append((code, lexer, formatter))
        return "highlighted body"

    monkeypatch.setattr(colors.pygments, "highlight", fake_highlight)

    result = color_formatter.format_body("original body", "application/json")

    assert result == "highlighted body"
    assert calls == [("original body", lexer, formatter)]


def test_format_body_returns_original_body_when_no_lexer_is_available(monkeypatch):
    color_formatter = object.__new__(ColorFormatter)

    monkeypatch.setattr(
        color_formatter,
        "get_lexer_for_body",
        lambda mime, body: None,
    )

    def unexpected_highlight(**kwargs):
        pytest.fail("pygments.highlight must not be called without a lexer")

    monkeypatch.setattr(colors.pygments, "highlight", unexpected_highlight)

    body = "plain unrecognized content"

    assert color_formatter.format_body(body, "application/x-unknown") == body
