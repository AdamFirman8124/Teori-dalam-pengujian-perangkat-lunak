# file: project/httpie/output/formatters/colors.py:46-72
# asked: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}
# gained: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}

import pytest

from httpie.context import Environment
from httpie.output.formatters.colors import (
    AUTO_STYLE,
    SOLARIZED_STYLE,
    ColorFormatter,
    SimplifiedHTTPLexer,
    Solarized256Style,
)
from pygments.formatters.terminal import TerminalFormatter
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.text import HttpLexer as PygmentsHttpLexer


def make_formatter(env, **kwargs):
    return ColorFormatter(env, format_options={}, **kwargs)


def test_disabled_when_no_colors():
    env = Environment(colors=0)
    formatter = make_formatter(env)
    assert formatter.enabled is False
    # Early return: none of the later attributes are set.
    assert not hasattr(formatter, 'formatter')
    assert not hasattr(formatter, 'http_lexer')
    assert not hasattr(formatter, 'explicit_json')


def test_auto_style_uses_terminal_formatter_even_with_256_colors():
    env = Environment(colors=256)
    formatter = make_formatter(env, color_scheme=AUTO_STYLE)
    assert formatter.enabled is True
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)
    assert not isinstance(formatter.formatter, Terminal256Formatter)
    assert formatter.explicit_json is False


def test_explicit_json_flag_is_stored():
    env = Environment(colors=256)
    formatter = make_formatter(env, explicit_json=True, color_scheme=AUTO_STYLE)
    assert formatter.explicit_json is True


def test_non_256_colors_fall_back_to_terminal_formatter():
    env = Environment(colors=8)
    formatter = make_formatter(env, color_scheme=SOLARIZED_STYLE)
    assert formatter.enabled is True
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)
    assert formatter.explicit_json is False


def test_256_colors_with_explicit_style_use_terminal256_formatter():
    env = Environment(colors=256)
    formatter = make_formatter(env, color_scheme=SOLARIZED_STYLE)
    assert formatter.enabled is True
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert formatter.formatter.style is Solarized256Style
    assert formatter.explicit_json is False
