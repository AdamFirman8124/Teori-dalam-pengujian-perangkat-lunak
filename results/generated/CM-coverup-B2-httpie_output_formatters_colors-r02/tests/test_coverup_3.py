# file: project/httpie/output/formatters/colors.py:81-89
# asked: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}

from httpie.output.formatters import colors
from httpie.output.formatters.colors import ColorFormatter


def test_format_body_highlights_when_lexer_is_available(monkeypatch):
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = object()
    lexer = object()
    calls = {}

    def fake_get_lexer_for_body(self, mime, body):
        calls["lexer_lookup"] = (self, mime, body)
        return lexer

    def fake_highlight(*, code, lexer, formatter):
        calls["highlight"] = (code, lexer, formatter)
        return "highlighted body"

    monkeypatch.setattr(
        ColorFormatter,
        "get_lexer_for_body",
        fake_get_lexer_for_body,
    )
    monkeypatch.setattr(colors.pygments, "highlight", fake_highlight)

    result = formatter.format_body('{"answer": 42}', "application/json")

    assert result == "highlighted body"
    assert calls["lexer_lookup"] == (
        formatter,
        "application/json",
        '{"answer": 42}',
    )
    assert calls["highlight"] == (
        '{"answer": 42}',
        lexer,
        formatter.formatter,
    )


def test_format_body_returns_original_body_when_no_lexer_is_available(
    monkeypatch,
):
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = object()
    calls = {}

    def fake_get_lexer_for_body(self, mime, body):
        calls["lexer_lookup"] = (self, mime, body)
        return None

    def unexpected_highlight(*args, **kwargs):
        raise AssertionError("pygments.highlight must not be called without a lexer")

    monkeypatch.setattr(
        ColorFormatter,
        "get_lexer_for_body",
        fake_get_lexer_for_body,
    )
    monkeypatch.setattr(colors.pygments, "highlight", unexpected_highlight)

    body = "unrecognized content"
    result = formatter.format_body(body, "application/x-unknown")

    assert result == body
    assert calls["lexer_lookup"] == (
        formatter,
        "application/x-unknown",
        body,
    )
