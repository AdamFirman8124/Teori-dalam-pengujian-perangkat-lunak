# file: project/httpie/output/formatters/colors.py:81-89
# asked: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}

import pygments
import pytest
from pygments.lexers.data import JsonLexer
from types import SimpleNamespace

from httpie.output.formatters.colors import ColorFormatter


def _make_formatter():
    env = SimpleNamespace(colors=1)
    formatter = ColorFormatter(env=env, format_options={})
    assert formatter.enabled is True
    assert hasattr(formatter, "formatter")
    return formatter


def test_format_body_with_lexer_highlights_body():
    formatter = _make_formatter()
    body = '{"hello": "world"}'

    result = formatter.format_body(body, "application/json")

    assert isinstance(result, str)
    assert result != body
    assert "\x1b[" in result
    assert "hello" in result
    assert "world" in result


def test_format_body_without_lexer_returns_body_unchanged():
    formatter = _make_formatter()
    body = "plain unhighlighted content \x00\x01"

    result = formatter.format_body(body, "application/x-unknown-xyz-123")

    assert result == body
    assert result is body


def test_format_body_calls_pygments_highlight_when_lexer_present(monkeypatch):
    formatter = _make_formatter()
    body = '{"a": 1}'
    fake_lexer = JsonLexer()
    calls = {}

    def fake_get_lexer(self, mime, body_arg):
        calls["mime"] = mime
        calls["body_arg"] = body_arg
        return fake_lexer

    def fake_highlight(code, lexer, formatter):
        calls["code"] = code
        calls["lexer"] = lexer
        calls["formatter"] = formatter
        return "highlighted:" + code

    monkeypatch.setattr(ColorFormatter, "get_lexer_for_body", fake_get_lexer)
    monkeypatch.setattr(pygments, "highlight", fake_highlight)

    result = formatter.format_body(body, "application/json")

    assert result == "highlighted:" + body
    assert calls == {
        "mime": "application/json",
        "body_arg": body,
        "code": body,
        "lexer": fake_lexer,
        "formatter": formatter.formatter,
    }


def test_format_body_skips_highlight_when_no_lexer(monkeypatch):
    formatter = _make_formatter()
    body = "do not highlight me"

    monkeypatch.setattr(
        ColorFormatter, "get_lexer_for_body", lambda self, mime, body_arg: None
    )

    def fail_highlight(*args, **kwargs):
        raise AssertionError("pygments.highlight must not be called without a lexer")

    monkeypatch.setattr(pygments, "highlight", fail_highlight)

    result = formatter.format_body(body, "application/x-unknown-xyz-123")

    assert result == body
    assert result is body
