# file: project/httpie/output/formatters/colors.py:91-99
# asked: {"lines": [95, 96, 97, 98], "branches": []}
# gained: {"lines": [95, 96, 97, 98], "branches": []}

import json
from types import SimpleNamespace

import pytest
from pygments.lexer import Lexer
from pygments.lexers.data import JsonLexer

from httpie.output.formatters.colors import ColorFormatter


@pytest.fixture
def color_env():
    """A minimal environment with colors enabled (256 colors)."""
    return SimpleNamespace(colors=256)


def make_formatter(env, **kwargs):
    """Create a ColorFormatter with the required format_options kwarg."""
    return ColorFormatter(env=env, format_options={}, **kwargs)


def test_get_lexer_for_body_json_mime(color_env):
    formatter = make_formatter(color_env, explicit_json=False)
    lexer = formatter.get_lexer_for_body(
        mime='application/json',
        body=json.dumps({'foo': 'bar'}),
    )
    assert lexer is not None
    assert isinstance(lexer, Lexer)
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_for_body_explicit_json(color_env):
    formatter = make_formatter(color_env, explicit_json=True)
    lexer = formatter.get_lexer_for_body(
        mime='text/plain',
        body=json.dumps({'foo': 'bar'}),
    )
    assert lexer is not None
    assert isinstance(lexer, Lexer)
    assert isinstance(lexer, JsonLexer)


def test_get_lexer_for_body_unknown_mime_returns_none(color_env):
    formatter = make_formatter(color_env, explicit_json=False)
    lexer = formatter.get_lexer_for_body(
        mime='application/x-unknown-type',
        body='not a recognized body',
    )
    assert lexer is None
