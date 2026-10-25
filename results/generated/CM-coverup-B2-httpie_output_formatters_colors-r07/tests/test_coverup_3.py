# file: project/httpie/output/formatters/colors.py:81-89
# asked: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}

import json

import pytest

from httpie.context import Environment
from httpie.output.formatters.colors import ColorFormatter


@pytest.fixture
def env_256():
    return Environment(colors=256)


def make_formatter(env, **kwargs):
    # FormatterPlugin requires 'format_options' in kwargs.
    return ColorFormatter(env=env, format_options={}, **kwargs)


def test_format_body_json_is_highlighted(env_256):
    formatter = make_formatter(env_256)
    body = json.dumps({'foo': 'bar', 'baz': [1, 2, 3]})
    result = formatter.format_body(body, 'application/json')

    # A lexer was found, so pygments.highlight() ran and produced
    # ANSI-escaped output different from the input body.
    assert result != body
    assert '\x1b[' in result
    # The original content must still be present in the highlighted output.
    assert 'foo' in result
    assert 'bar' in result


def test_format_body_unknown_mime_returns_body_unchanged(env_256):
    formatter = make_formatter(env_256)
    body = 'just some plain text'
    result = formatter.format_body(body, 'application/x-httpie-unknown-type')

    # No lexer for this mime type: body is returned as-is (no highlighting).
    assert result == body
    assert '\x1b[' not in result


def test_format_body_no_lexer_branch(env_256, monkeypatch):
    formatter = make_formatter(env_256)
    body = '{"key": "value"}'

    # Force the falsy-lexer branch deterministically.
    monkeypatch.setattr(
        formatter, 'get_lexer_for_body', lambda mime, body: None
    )

    assert formatter.format_body(body, 'application/json') == body


def test_format_body_explicit_json_flag_forces_json_lexer(env_256):
    formatter = make_formatter(env_256, explicit_json=True)
    body = '{"key": "value"}'

    lexer = formatter.get_lexer_for_body('text/plain', body)
    assert lexer is not None
    assert 'json' in str(lexer).lower()

    result = formatter.format_body(body, 'text/plain')
    assert result != body
    assert 'key' in result
