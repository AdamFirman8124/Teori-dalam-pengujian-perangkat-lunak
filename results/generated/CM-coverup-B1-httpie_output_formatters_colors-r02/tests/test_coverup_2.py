# file: project/httpie/output/formatters/colors.py:46-72
# asked: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}
# gained: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}

import types
from pygments.formatters.terminal import TerminalFormatter
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.text import HttpLexer as PygmentsHttpLexer
from httpie.output.formatters.colors import (
    AUTO_STYLE,
    DEFAULT_STYLE,
    ColorFormatter,
    SimplifiedHTTPLexer,
)


def _make_env(colors):
    return types.SimpleNamespace(colors=colors)


def _make_formatter(colors, **kwargs):
    env = _make_env(colors)
    kwargs.setdefault("format_options", {})
    return ColorFormatter(env=env, **kwargs)


def test_disabled_when_no_colors():
    fmt = _make_formatter(0)
    assert fmt.enabled is False
    assert not hasattr(fmt, "formatter")
    assert not hasattr(fmt, "http_lexer")


def test_disabled_when_colors_none():
    fmt = _make_formatter(None)
    assert fmt.enabled is False


def test_auto_style_with_256_colors_uses_terminal_formatter():
    fmt = _make_formatter(256, color_scheme=AUTO_STYLE)
    assert fmt.enabled is True
    assert isinstance(fmt.formatter, TerminalFormatter)
    assert not isinstance(fmt.formatter, Terminal256Formatter)
    assert isinstance(fmt.http_lexer, PygmentsHttpLexer)
    assert fmt.explicit_json is False


def test_auto_style_with_low_colors_uses_terminal_formatter():
    fmt = _make_formatter(8, color_scheme=AUTO_STYLE, explicit_json=True)
    assert fmt.enabled is True
    assert isinstance(fmt.formatter, TerminalFormatter)
    assert isinstance(fmt.http_lexer, PygmentsHttpLexer)
    assert fmt.explicit_json is True


def test_default_style_with_256_colors_uses_terminal_formatter():
    assert DEFAULT_STYLE == AUTO_STYLE
    fmt = _make_formatter(256)
    assert isinstance(fmt.formatter, TerminalFormatter)
    assert isinstance(fmt.http_lexer, PygmentsHttpLexer)
    assert fmt.explicit_json is False


def test_non_auto_low_colors_falls_back_to_terminal_formatter():
    fmt = _make_formatter(8, color_scheme="monokai")
    assert fmt.enabled is True
    assert isinstance(fmt.formatter, TerminalFormatter)
    assert isinstance(fmt.http_lexer, PygmentsHttpLexer)
    assert fmt.explicit_json is False


def test_non_auto_256_colors_uses_terminal256_formatter():
    fmt = _make_formatter(256, color_scheme="monokai", explicit_json=True)
    assert fmt.enabled is True
    assert isinstance(fmt.formatter, Terminal256Formatter)
    assert isinstance(fmt.http_lexer, SimplifiedHTTPLexer)
    assert fmt.explicit_json is True
