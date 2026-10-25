# file: project/httpie/output/formatters/colors.py:81-89
# asked: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}

from httpie.output.formatters import colors


def test_format_body_highlights_when_lexer_is_available(monkeypatch):
    formatter = colors.ColorFormatter.__new__(colors.ColorFormatter)
    lexer = object()
    formatter_backend = object()
    formatter.formatter = formatter_backend
    calls = []

    def fake_get_lexer(mime, body):
        calls.append(("get_lexer", mime, body))
        return lexer

    def fake_highlight(*, code, lexer, formatter):
        calls.append(("highlight", code, lexer, formatter))
        return "highlighted body"

    monkeypatch.setattr(formatter, "get_lexer_for_body", fake_get_lexer)
    monkeypatch.setattr(colors.pygments, "highlight", fake_highlight)

    result = formatter.format_body("original body", "application/json")

    assert result == "highlighted body"
    assert calls == [
        ("get_lexer", "application/json", "original body"),
        ("highlight", "original body", lexer, formatter_backend),
    ]


def test_format_body_returns_body_unchanged_when_no_lexer_is_available(
    monkeypatch,
):
    formatter = colors.ColorFormatter.__new__(colors.ColorFormatter)
    calls = []

    def fake_get_lexer(mime, body):
        calls.append(("get_lexer", mime, body))
        return None

    def unexpected_highlight(**kwargs):
        raise AssertionError("pygments.highlight must not be called without a lexer")

    monkeypatch.setattr(formatter, "get_lexer_for_body", fake_get_lexer)
    monkeypatch.setattr(colors.pygments, "highlight", unexpected_highlight)

    result = formatter.format_body("plain body", "application/octet-stream")

    assert result == "plain body"
    assert calls == [
        ("get_lexer", "application/octet-stream", "plain body"),
    ]
