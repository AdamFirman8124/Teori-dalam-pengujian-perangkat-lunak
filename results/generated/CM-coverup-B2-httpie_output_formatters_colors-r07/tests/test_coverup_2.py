# file: project/httpie/output/formatters/colors.py:46-72
# asked: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}
# gained: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}

from pygments.formatters.terminal import TerminalFormatter
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.text import HttpLexer as PygmentsHttpLexer

from httpie.context import Environment
from httpie.output.formatters.colors import (
    AUTO_STYLE,
    ColorFormatter,
    SimplifiedHTTPLexer,
)


def _make_env(colors):
    return Environment(colors=colors)


def test_disabled_when_no_colors():
    env = _make_env(colors=0)
    fmt = ColorFormatter(env=env, format_options={})
    assert fmt.enabled is False
    assert not hasattr(fmt, "formatter")
    assert not hasattr(fmt, "http_lexer")


def test_disabled_when_colors_none(monkeypatch):
    env = _make_env(colors=256)
    monkeypatch.setattr(env, "colors", None)
    fmt = ColorFormatter(env=env, format_options={})
    assert fmt.enabled is False


def test_auto_style_with_256_colors():
    env = _make_env(colors=256)
    fmt = ColorFormatter(env=env, format_options={}, color_scheme=AUTO_STYLE)
    assert fmt.enabled is True
    assert isinstance(fmt.formatter, TerminalFormatter)
    assert isinstance(fmt.http_lexer, PygmentsHttpLexer)
    assert fmt.explicit_json is False


def test_auto_style_with_few_colors():
    env = _make_env(colors=8)
    fmt = ColorFormatter(
        env=env, format_options={}, color_scheme=AUTO_STYLE, explicit_json=True
    )
    assert fmt.enabled is True
    assert isinstance(fmt.formatter, TerminalFormatter)
    assert isinstance(fmt.http_lexer, PygmentsHttpLexer)
    assert fmt.explicit_json is True
    assert fmt.formatter is fmt.formatter
    assert fmt.http_lexer is fmt.http_lexer


def test_explicit_style_with_few_colors_uses_terminal_formatter():
    env = _make_env(colors=8)
    fmt = ColorFormatter(env=env, format_options={}, color_scheme="monokai")
    assert fmt.enabled is True
    assert isinstance(fmt.formatter, TerminalFormatter)
    assert isinstance(fmt.http_lexer, PygmentsHttpLexer)
    assert fmt.explicit_json is False


def test_explicit_style_with_256_colors_uses_terminal256_formatter():
    env = _make_env(colors=256)
    fmt = ColorFormatter(
        env=env, format_options={}, color_scheme="monokai", explicit_json=True
    )
    assert fmt.enabled is True
    assert isinstance(fmt.formatter, Terminal256Formatter)
    assert isinstance(fmt.http_lexer, SimplifiedHTTPLexer)
    assert fmt.explicit_json is True
