# file: project/httpie/output/formatters/colors.py:81-89
# asked: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}

import httpie.output.formatters.colors as colors
from httpie.output.formatters.colors import ColorFormatter


def test_format_body_highlights_when_lexer_is_available(monkeypatch):
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = object()
    lexer = object()
    calls = {}

    def fake_get_lexer(self, mime, body):
        calls["lexer_lookup"] = (mime, body)
        return lexer

    def fake_highlight(*, code, lexer, formatter):
        calls["highlight"] = (code, lexer, formatter)
        return "highlighted body"

    monkeypatch.setattr(ColorFormatter, "get_lexer_for_body", fake_get_lexer)
    monkeypatch.setattr(colors.pygments, "highlight", fake_highlight)

    result = formatter.format_body('{"answer": 42}', "application/json")

    assert calls["lexer_lookup"] == ("application/json", '{"answer": 42}')
    assert calls["highlight"] == (
        '{"answer": 42}',
        lexer,
        formatter.formatter,
    )
    assert result == "highlighted body"


def test_format_body_returns_original_body_when_no_lexer_is_available(
    monkeypatch,
):
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = object()
    calls = []

    def fake_get_lexer(self, mime, body):
        calls.append((mime, body))
        return None

    def unexpected_highlight(**kwargs):
        raise AssertionError("pygments.highlight must not be called")

    monkeypatch.setattr(ColorFormatter, "get_lexer_for_body", fake_get_lexer)
    monkeypatch.setattr(colors.pygments, "highlight", unexpected_highlight)

    body = "unrecognized content"
    result = formatter.format_body(body, "application/octet-stream")

    assert calls == [("application/octet-stream", body)]
    assert result == body
