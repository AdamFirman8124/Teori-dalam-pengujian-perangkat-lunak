# file: project/httpie/output/formatters/colors.py:91-99
# asked: {"lines": [95, 96, 97, 98], "branches": []}
# gained: {"lines": [95, 96, 97, 98], "branches": []}

import pytest
from pygments.lexer import Lexer
from pygments.lexers.data import JsonLexer

from httpie.output.formatters import colors as colors_module
from httpie.output.formatters.colors import ColorFormatter


def _make_formatter(explicit_json=False):
    """Build a ColorFormatter without touching Environment/plugin state."""
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.explicit_json = explicit_json
    return formatter


def test_get_lexer_for_body_forwards_all_arguments(monkeypatch):
    calls = {}
    sentinel = object()

    def fake_get_lexer(mime, explicit_json, body):
        calls['mime'] = mime
        calls['explicit_json'] = explicit_json
        calls['body'] = body
        return sentinel

    monkeypatch.setattr(colors_module, 'get_lexer', fake_get_lexer)
    formatter = _make_formatter(explicit_json=True)

    result = formatter.get_lexer_for_body(
        mime='application/json',
        body='{"a": 1}',
    )

    assert result is sentinel
    assert calls == {
        'mime': 'application/json',
        'explicit_json': True,
        'body': '{"a": 1}',
    }


def test_get_lexer_for_body_forwards_explicit_json_false(monkeypatch):
    calls = {}

    def fake_get_lexer(mime, explicit_json, body):
        calls['mime'] = mime
        calls['explicit_json'] = explicit_json
        calls['body'] = body
        return None

    monkeypatch.setattr(colors_module, 'get_lexer', fake_get_lexer)
    formatter = _make_formatter(explicit_json=False)

    result = formatter.get_lexer_for_body(mime='text/plain', body='hello')

    assert result is None
    assert calls == {
        'mime': 'text/plain',
        'explicit_json': False,
        'body': 'hello',
    }


def test_get_lexer_for_body_returns_json_lexer_for_json_mime():
    formatter = _make_formatter(explicit_json=False)

    lexer = formatter.get_lexer_for_body(
        mime='application/json',
        body='{"a": 1}',
    )

    assert lexer is not None
    assert isinstance(lexer, JsonLexer)
    assert isinstance(lexer, Lexer)
