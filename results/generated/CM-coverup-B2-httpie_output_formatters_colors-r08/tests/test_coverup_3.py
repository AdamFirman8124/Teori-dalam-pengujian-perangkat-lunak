# file: project/httpie/output/formatters/colors.py:81-89
# asked: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}

import pygments
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers import JsonLexer

from httpie.output.formatters.colors import ColorFormatter


def _make_formatter():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = TerminalFormatter()
    formatter.explicit_json = False
    return formatter


def test_format_body_highlights_when_lexer_found(monkeypatch):
    formatter = _make_formatter()
    lexer = JsonLexer()
    seen = {}

    orig_highlight = pygments.highlight

    def fake_highlight(code=None, lexer=None, formatter=None, **kwargs):
        seen["code"] = code
        seen["lexer"] = lexer
        seen["formatter"] = formatter
        return orig_highlight(code=code, lexer=lexer, formatter=formatter)

    monkeypatch.setattr(formatter, "get_lexer_for_body", lambda mime, body: lexer)
    monkeypatch.setattr(pygments, "highlight", fake_highlight)

    body = '{"a": 1}'
    mime = "application/json"
    result = formatter.format_body(body, mime)

    assert seen["code"] == body
    assert seen["lexer"] is lexer
    assert seen["formatter"] is formatter.formatter
    assert isinstance(result, str)
    assert result != body
    assert "a" in result


def test_format_body_returns_body_unchanged_when_no_lexer(monkeypatch):
    formatter = _make_formatter()
    monkeypatch.setattr(formatter, "get_lexer_for_body", lambda mime, body: None)

    called = []
    orig_highlight = pygments.highlight

    def fail_highlight(*args, **kwargs):
        called.append(True)
        return orig_highlight(*args, **kwargs)

    monkeypatch.setattr(pygments, "highlight", fail_highlight)

    body = "plain body without lexer"
    result = formatter.format_body(body, "unknown/unknown-type")

    assert result == body
    assert called == []
