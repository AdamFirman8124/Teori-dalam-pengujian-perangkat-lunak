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
    Solarized256Style,
)


def test_color_formatter_is_disabled_when_terminal_has_no_colors():
    format_options = {}
    formatter = ColorFormatter(
        env=Environment(colors=0),
        explicit_json=True,
        format_options=format_options,
    )

    assert formatter.enabled is False
    assert formatter.format_options is format_options
    assert formatter.kwargs == {"format_options": format_options}
    assert not hasattr(formatter, "explicit_json")
    assert not hasattr(formatter, "formatter")
    assert not hasattr(formatter, "http_lexer")


def test_color_formatter_uses_basic_formatter_for_auto_style():
    formatter = ColorFormatter(
        env=Environment(colors=256),
        explicit_json=True,
        color_scheme=AUTO_STYLE,
        format_options={},
    )

    assert formatter.enabled is True
    assert formatter.explicit_json is True
    assert type(formatter.formatter) is TerminalFormatter
    assert type(formatter.http_lexer) is PygmentsHttpLexer


def test_color_formatter_uses_basic_formatter_when_256_colors_unavailable(
    monkeypatch,
):
    def fail_if_called(_color_scheme):
        raise AssertionError("get_style_class must not be used without 256 colors")

    monkeypatch.setattr(
        ColorFormatter,
        "get_style_class",
        staticmethod(fail_if_called),
    )

    formatter = ColorFormatter(
        env=Environment(colors=16),
        explicit_json=False,
        color_scheme="custom-style",
        format_options={},
    )

    assert formatter.enabled is True
    assert formatter.explicit_json is False
    assert type(formatter.formatter) is TerminalFormatter
    assert type(formatter.http_lexer) is PygmentsHttpLexer


def test_color_formatter_uses_256_formatter_for_explicit_style(monkeypatch):
    requested_schemes = []

    def get_style_class(color_scheme):
        requested_schemes.append(color_scheme)
        return Solarized256Style

    monkeypatch.setattr(
        ColorFormatter,
        "get_style_class",
        staticmethod(get_style_class),
    )

    formatter = ColorFormatter(
        env=Environment(colors=256),
        explicit_json=True,
        color_scheme="custom-style",
        format_options={},
    )

    assert requested_schemes == ["custom-style"]
    assert formatter.enabled is True
    assert formatter.explicit_json is True
    assert type(formatter.formatter) is Terminal256Formatter
    assert formatter.formatter.style is Solarized256Style
    assert type(formatter.http_lexer) is SimplifiedHTTPLexer
