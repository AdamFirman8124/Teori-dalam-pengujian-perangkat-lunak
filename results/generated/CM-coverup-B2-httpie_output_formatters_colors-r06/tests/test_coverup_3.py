# file: project/httpie/output/formatters/colors.py:81-89
# asked: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84], [83, 89]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 89], "branches": [[83, 84]]}

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


def test_format_body_plain_text_gets_no_color(env_256):
    formatter = make_formatter(env_256)
    body = 'just some plain text'
    result = formatter.format_body(body, 'text/plain')

    # A (plain-text) lexer is found and pygments.highlight() runs;
    # pygments' default 'ensurenl' option appends a trailing newline,
    # but plain text produces no ANSI color escape codes.
    assert result == body + '\n'
    assert '\x1b[' not in result


def test_format_body_explicit_json_flag_forces_json_lexer(env_256):
    formatter = make_formatter(env_256, explicit_json=True)
    body = '{"key": "value"}'
    result = formatter.format_body(body, 'text/plain')

    # With explicit_json=True, a JSON-looking body gets highlighted
    # even though the mime type is text/plain.
    assert result != body
    assert '\x1b[' in result
    assert 'key' in result
