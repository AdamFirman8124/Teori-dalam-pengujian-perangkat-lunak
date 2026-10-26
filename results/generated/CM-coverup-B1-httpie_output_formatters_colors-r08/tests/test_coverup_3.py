# file: project/httpie/output/formatters/colors.py:81-89
# asked: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}

from types import SimpleNamespace

import pytest
from pygments.lexers.data import JsonLexer

import httpie.output.formatters.colors as colors_module
from httpie.output.formatters.colors import ColorFormatter


@pytest.fixture
def formatter():
    env = SimpleNamespace(colors=256)
    return ColorFormatter(env=env, format_options={})


def test_format_body_highlights_body_when_lexer_is_found(formatter, monkeypatch):
    body = '{"answer": 42}'
    lexer = JsonLexer()
    captured = {}

    def fake_get_lexer(mime, explicit_json, body):
        captured['get_lexer'] = (mime, explicit_json, body)
        return lexer

    def fake_highlight(code, lexer, formatter):
        captured['highlight'] = (code, lexer, formatter)
        return '<highlighted>'

    monkeypatch.setattr(colors_module, 'get_lexer', fake_get_lexer)
    monkeypatch.setattr(colors_module.pygments, 'highlight', fake_highlight)

    result = formatter.format_body(body, 'application/json')

    assert result == '<highlighted>'
    assert captured['get_lexer'] == ('application/json', False, body)
    assert captured['highlight'] == (body, lexer, formatter.formatter)


def test_format_body_applies_real_pygments_highlighting(formatter, monkeypatch):
    body = '{"answer": 42}'
    monkeypatch.setattr(
        colors_module,
        'get_lexer',
        lambda mime, explicit_json, body: JsonLexer(),
    )

    result = formatter.format_body(body, 'application/json')

    assert result != body
    assert '\x1b[' in result


def test_format_body_returns_body_unchanged_when_no_lexer(formatter, monkeypatch):
    body = 'not highlighted'
    monkeypatch.setattr(
        colors_module,
        'get_lexer',
        lambda mime, explicit_json, body: None,
    )

    def fail(**kwargs):
        raise AssertionError('pygments.highlight must not be called')

    monkeypatch.setattr(colors_module.pygments, 'highlight', fail)

    assert formatter.format_body(body, 'text/plain') == body


def test_format_body_passes_explicit_json_flag(monkeypatch):
    env = SimpleNamespace(colors=256)
    fmt = ColorFormatter(env=env, explicit_json=True, format_options={})
    seen = {}

    def fake_get_lexer(mime, explicit_json, body):
        seen['explicit_json'] = explicit_json
        return None

    monkeypatch.setattr(colors_module, 'get_lexer', fake_get_lexer)

    body = '{"a": 1}'
    assert fmt.format_body(body, 'text/plain') == body
    assert seen['explicit_json'] is True
