# file: project/httpie/output/formatters/colors.py:46-72
# asked: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}
# gained: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}

"""Tests for httpie.output.formatters.colors.ColorFormatter.__init__.

Covers the previously untested lines 53-72:
  * line 53:  super().__init__(**kwargs)
  * 55-57:    early return when env.colors is falsy
  * 59-63:    auto style OR non-256 colors -> PygmentsHttpLexer + TerminalFormatter
  * 65-67:    non-auto style with 256 colors -> SimplifiedHTTPLexer + Terminal256Formatter
  * 70-72:    attribute assignments (explicit_json, formatter, http_lexer)

These tests are pure: they only build local Environment/ColorFormatter objects
and never mutate global state, so no monkeypatching/cleanup is required.
"""
import pygments.styles
from pygments.formatters.terminal import TerminalFormatter
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.text import HttpLexer as PygmentsHttpLexer

from httpie.context import Environment
from httpie.output.formatters.colors import (
    AUTO_STYLE,
    ColorFormatter,
    SimplifiedHTTPLexer,
    Solarized256Style,
)


def make_color_formatter(colors, **kwargs):
    """Instantiate ColorFormatter with a fully controlled Environment.

    FormatterPlugin.__init__ requires 'format_options' in kwargs, so it is
    always provided here (this is what makes line 53 execute).
    """
    env = Environment(colors=colors)
    return ColorFormatter(env, format_options={}, **kwargs)


def test_super_init_runs_and_no_colors_disables_formatter():
    formatter = make_color_formatter(colors=0)

    # Line 53: FormatterPlugin.__init__ ran and consumed the kwargs.
    assert formatter.kwargs['format_options'] == {}
    assert formatter.format_options == {}

    # Lines 55-57: early return disabled the formatter and skipped the rest.
    assert formatter.enabled is False
    assert not hasattr(formatter, 'explicit_json')
    assert not hasattr(formatter, 'formatter')
    assert not hasattr(formatter, 'http_lexer')


def test_auto_style_with_256_colors_uses_terminal_formatter():
    # use_auto_style is True -> short-circuits the 'or' even with 256 colors.
    formatter = make_color_formatter(colors=256, color_scheme=AUTO_STYLE)

    assert formatter.enabled is True
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)
    # Lines 70-72: defaults assigned.
    assert formatter.explicit_json is False


def test_default_style_with_non_256_colors_uses_terminal_formatter():
    # No color_scheme passed -> default parameter value is exercised;
    # colors != 256 forces the TerminalFormatter branch on any platform
    # (DEFAULT_STYLE is 'fruity' on Windows, 'auto' elsewhere).
    formatter = make_color_formatter(colors=8)

    assert formatter.enabled is True
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)
    assert formatter.explicit_json is False


def test_256_colors_with_named_style_uses_256_formatter():
    # else branch (lines 65-67): SimplifiedHTTPLexer + Terminal256Formatter
    # styled with the resolved pygments style; explicit_json forwarded.
    formatter = make_color_formatter(
        colors=256, color_scheme='monokai', explicit_json=True
    )

    assert formatter.enabled is True
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert formatter.formatter.style is pygments.styles.get_style_by_name('monokai')
    assert formatter.explicit_json is True


def test_256_colors_with_solarized_falls_back_to_solarized_style():
    # 'solarized' is not a pygments style name, so get_style_class()
    # (called on line 67) must fall back to Solarized256Style.
    formatter = make_color_formatter(colors=256, color_scheme='solarized')

    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert formatter.formatter.style is Solarized256Style


def test_get_style_class_resolves_known_pygments_style():
    assert (
        ColorFormatter.get_style_class('monokai')
        is pygments.styles.get_style_by_name('monokai')
    )


def test_get_style_class_falls_back_to_solarized():
    assert ColorFormatter.get_style_class('solarized') is Solarized256Style
