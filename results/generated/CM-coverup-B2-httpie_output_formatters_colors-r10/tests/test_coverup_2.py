# file: project/httpie/output/formatters/colors.py:46-72
# asked: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}
# gained: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}

import pytest
from pygments.formatters.terminal import TerminalFormatter
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.text import HttpLexer as PygmentsHttpLexer

from httpie.output.formatters.colors import (
    AUTO_STYLE,
    SOLARIZED_STYLE,
    ColorFormatter,
    SimplifiedHTTPLexer,
)


class FakeEnvironment:
    """Minimal stand-in for httpie.context.Environment."""

    def __init__(self, colors):
        self.colors = colors


def make_formatter(env, **kwargs):
    kwargs.setdefault('format_options', {})
    return ColorFormatter(env, **kwargs)


def test_init_disabled_when_colors_falsy():
    env = FakeEnvironment(colors=False)
    formatter = make_formatter(env, explicit_json=True, color_scheme=SOLARIZED_STYLE)

    assert formatter.enabled is False
    # Early return: the rest of __init__ must not have run.
    assert not hasattr(formatter, 'formatter')
    assert not hasattr(formatter, 'http_lexer')
    assert not hasattr(formatter, 'explicit_json')


def test_init_disabled_when_colors_zero():
    env = FakeEnvironment(colors=0)
    formatter = make_formatter(env)

    assert formatter.enabled is False
    assert not hasattr(formatter, 'formatter')


def test_init_auto_style_uses_pygments_http_lexer_and_terminal_formatter():
    env = FakeEnvironment(colors=256)
    formatter = make_formatter(env, color_scheme=AUTO_STYLE)

    assert formatter.enabled is True
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)
    assert not isinstance(formatter.formatter, Terminal256Formatter)
    assert formatter.explicit_json is False


def test_init_non_256_colors_uses_pygments_http_lexer_and_terminal_formatter():
    env = FakeEnvironment(colors=8)
    formatter = make_formatter(env, color_scheme=SOLARIZED_STYLE, explicit_json=True)

    assert formatter.enabled is True
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)
    assert formatter.explicit_json is True


def test_init_256_colors_with_explicit_style_uses_simplified_lexer_and_256_formatter():
    env = FakeEnvironment(colors=256)
    formatter = make_formatter(env, color_scheme=SOLARIZED_STYLE, explicit_json=True)

    assert formatter.enabled is True
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert formatter.formatter.style == ColorFormatter.get_style_class(SOLARIZED_STYLE)
    assert formatter.explicit_json is True


def test_init_stores_kwargs_via_super():
    env = FakeEnvironment(colors=256)
    formatter = make_formatter(env, color_scheme=AUTO_STYLE, format_options={'a': 1})

    assert formatter.kwargs['format_options'] == {'a': 1}
    assert formatter.format_options == {'a': 1}
