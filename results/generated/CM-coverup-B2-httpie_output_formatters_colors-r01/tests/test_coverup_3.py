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


def test_format_body_no_lexer_returns_body_unchanged(env_256):
    formatter = make_formatter(env_256)
    body = 'just some plain text'
    # Use a mime type for which Pygments has no lexer (and no
    # json/xml fallback for this top-level type), so
    # get_lexer_for_body() returns None and format_body()
    # returns the body untouched. Note: 'text/plain' cannot be
    # used here because Pygments has a TextLexer for it, which
    # goes through pygments.highlight() and appends a newline.
    result = formatter.format_body(body, 'httpietest/unknown-format')

    assert result == body
    assert '\x1b[' not in result


def test_format_body_explicit_json_flag_forces_json_lexer(env_256):
    formatter = make_formatter(env_256, explicit_json=True)
    body = '{"key": "value"}'
    result = formatter.format_body(body, 'httpietest/unknown-format')

    # With explicit_json=True, a JSON-looking body gets highlighted
    # even though no lexer exists for the mime type.
    assert result != body
    assert '\x1b[' in result
    assert 'key' in result
    assert 'value' in result
