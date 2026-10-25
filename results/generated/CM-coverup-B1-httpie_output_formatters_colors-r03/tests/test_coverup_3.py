# file: project/httpie/output/formatters/colors.py:81-89
# asked: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}

import json

import pytest

from httpie.context import Environment
from httpie.output.formatters import colors as colors_module
from httpie.output.formatters.colors import ColorFormatter


@pytest.fixture
def env_256():
    return Environment(colors=256)


def make_formatter(env, **kwargs):
    # FormatterPlugin requires 'format_options' in kwargs.
    return ColorFormatter(env=env, format_options={}, **kwargs)


def test_format_body_highlights_json(env_256):
    formatter = make_formatter(env_256)
    body = json.dumps({'foo': 'bar', 'baz': [1, 2, 3]})

    result = formatter.format_body(body, 'application/json')

    # A lexer was found, so pygments.highlight() ran and produced
    # ANSI-escaped output.
    assert result != body
    assert '\x1b[' in result
    assert 'foo' in result
    assert 'bar' in result


def test_format_body_returns_body_unchanged_when_no_lexer(env_256, monkeypatch):
    formatter = make_formatter(env_256)
    body = 'just some plain text'

    # Force the "no lexer" branch deterministically.
    monkeypatch.setattr(colors_module, 'get_lexer', lambda **kwargs: None)

    result = formatter.format_body(body, 'text/plain')

    assert result == body
    assert '\x1b[' not in result


def test_format_body_passes_mime_and_body_to_lexer_lookup(env_256, monkeypatch):
    formatter = make_formatter(env_256)
    body = '{"key": "value"}'
    seen = {}

    def fake_get_lexer(mime, explicit_json, body):
        seen['mime'] = mime
        seen['explicit_json'] = explicit_json
        seen['body'] = body
        return None

    monkeypatch.setattr(colors_module, 'get_lexer', fake_get_lexer)

    result = formatter.format_body(body, 'application/json')

    assert result == body
    assert seen == {
        'mime': 'application/json',
        'explicit_json': False,
        'body': body,
    }


def test_format_body_explicit_json_flag_forces_json_lexer(env_256):
    formatter = make_formatter(env_256, explicit_json=True)
    body = '{"key": "value"}'

    result = formatter.format_body(body, 'text/plain')

    # With explicit_json=True, a JSON-looking body gets highlighted
    # even though the mime type is text/plain.
    assert result != body
    assert '\x1b[' in result
    assert 'key' in result
