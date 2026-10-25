# file: project/httpie/output/formatters/colors.py:46-72
# asked: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}
# gained: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}

import pytest
from pygments.formatters.terminal import TerminalFormatter
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.text import HttpLexer as PygmentsHttpLexer
from pygments.styles import get_style_by_name

from httpie.output.formatters.colors import (
    AUTO_STYLE,
    ColorFormatter,
    SimplifiedHTTPLexer,
    Solarized256Style,
)


class FakeEnv:
    """Minimal stand-in for httpie.context.Environment.

    ColorFormatter.__init__ only reads ``env.colors``, so this avoids
    constructing a full Environment (and any associated global state).
    """

    def __init__(self, colors):
        self.colors = colors


def make_formatter(env, **kwargs):
    # FormatterPlugin.__init__ requires a 'format_options' kwarg.
    kwargs.setdefault('format_options', {})
    return ColorFormatter(env, **kwargs)


@pytest.mark.parametrize('colors', [0, False, None])
def test_disabled_when_colors_are_disabled(colors):
    formatter = make_formatter(FakeEnv(colors))

    assert formatter.enabled is False
    # The early return must happen before any of the later attributes are set.
    assert not hasattr(formatter, 'explicit_json')
    assert not hasattr(formatter, 'formatter')
    assert not hasattr(formatter, 'http_lexer')


@pytest.mark.parametrize('colors', [256, 8])
def test_auto_style_uses_pygments_http_lexer_and_terminal_formatter(colors):
    formatter = make_formatter(
        FakeEnv(colors),
        color_scheme=AUTO_STYLE,
        explicit_json=True,
    )

    assert formatter.enabled is True
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)
    assert not isinstance(formatter.formatter, Terminal256Formatter)
    assert formatter.explicit_json is True
    assert formatter.format_options == {}


def test_non_256_colors_with_explicit_style_uses_terminal_formatter():
    formatter = make_formatter(FakeEnv(8), color_scheme='solarized')

    assert formatter.enabled is True
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)
    assert not isinstance(formatter.formatter, Terminal256Formatter)
    assert formatter.explicit_json is False


def test_256_colors_with_solarized_style_uses_simplified_lexer():
    formatter = make_formatter(FakeEnv(256), color_scheme='solarized')

    assert formatter.enabled is True
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)
    # Terminal256Formatter stores the style *class*, not an instance.
    assert isinstance(formatter.formatter.style, type)
    assert issubclass(formatter.formatter.style, Solarized256Style)
    assert formatter.explicit_json is False


def test_256_colors_with_known_pygments_style():
    formatter = make_formatter(FakeEnv(256), color_scheme='monokai')

    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert isinstance(formatter.formatter.style, type)
    assert issubclass(formatter.formatter.style, get_style_by_name('monokai'))


def test_256_colors_with_unknown_style_falls_back_to_solarized():
    formatter = make_formatter(
        FakeEnv(256),
        color_scheme='definitely-not-a-real-pygments-style',
    )

    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert isinstance(formatter.formatter.style, type)
    assert issubclass(formatter.formatter.style, Solarized256Style)
