# file: project/httpie/output/formatters/colors.py:81-89
# asked: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}

import re

import pygments
import pytest
from pygments.lexers.data import JsonLexer

from httpie.context import Environment
from httpie.output.formatters.colors import ColorFormatter


def _make_formatter():
    formatter = ColorFormatter(
        env=Environment(colors=256),
        format_options={},
    )
    assert formatter.enabled
    assert formatter.formatter is not None
    return formatter


def test_format_body_without_lexer_returns_body_unchanged(monkeypatch):
    formatter = _make_formatter()
    body = '{"key": "value"}'
    monkeypatch.setattr(
        ColorFormatter,
        'get_lexer_for_body',
        lambda self, mime, body: None,
    )

    result = formatter.format_body(body, 'application/json')

    assert result == body


def test_format_body_with_lexer_calls_pygments_highlight(monkeypatch):
    formatter = _make_formatter()
    body = '{"key": "value"}'
    lexer = JsonLexer()
    calls = {}

    def fake_highlight(code, lexer, formatter):
        calls['code'] = code
        calls['lexer'] = lexer
        calls['formatter'] = formatter
        return 'HIGHLIGHTED'

    monkeypatch.setattr(
        ColorFormatter,
        'get_lexer_for_body',
        lambda self, mime, body: lexer,
    )
    monkeypatch.setattr(pygments, 'highlight', fake_highlight)

    result = formatter.format_body(body, 'application/json')

    assert result == 'HIGHLIGHTED'
    assert calls == {
        'code': body,
        'lexer': lexer,
        'formatter': formatter.formatter,
    }


def test_format_body_with_real_lexer_produces_highlighted_output(monkeypatch):
    formatter = _make_formatter()
    body = '{"key": "value"}'
    monkeypatch.setattr(
        ColorFormatter,
        'get_lexer_for_body',
        lambda self, mime, body: JsonLexer(),
    )

    result = formatter.format_body(body, 'application/json')

    assert result != body
    assert '\x1b[' in result
    plain = re.sub(r'\x1b\[[0-9;]*m', '', result)
    assert '"key"' in plain
    assert '"value"' in plain
