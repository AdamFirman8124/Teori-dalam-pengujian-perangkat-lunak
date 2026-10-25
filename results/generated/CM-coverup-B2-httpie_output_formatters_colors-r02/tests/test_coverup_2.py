# file: project/httpie/output/formatters/colors.py:46-72
# asked: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}
# gained: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}

from types import SimpleNamespace

import pytest
from pygments.formatters.terminal import TerminalFormatter
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.text import HttpLexer as PygmentsHttpLexer

from httpie.output.formatters.colors import (
    AUTO_STYLE,
    ColorFormatter,
    SimplifiedHTTPLexer,
)


def test_color_formatter_is_disabled_when_environment_has_no_colors():
    format_options = {"headers": True}
    formatter = ColorFormatter(
        env=SimpleNamespace(colors=0),
        explicit_json=True,
        color_scheme="monokai",
        format_options=format_options,
    )

    assert formatter.enabled is False
    assert formatter.kwargs == {"format_options": format_options}
    assert formatter.format_options is format_options
    assert not hasattr(formatter, "explicit_json")
    assert not hasattr(formatter, "formatter")
    assert not hasattr(formatter, "http_lexer")


@pytest.mark.parametrize(
    ("colors", "color_scheme"),
    [
        (256, AUTO_STYLE),
        (16, "monokai"),
    ],
)
def test_color_formatter_uses_basic_terminal_formatter(colors, color_scheme):
    format_options = {}
    formatter = ColorFormatter(
        env=SimpleNamespace(colors=colors),
        explicit_json=True,
        color_scheme=color_scheme,
        format_options=format_options,
    )

    assert formatter.enabled is True
    assert formatter.explicit_json is True
    assert type(formatter.formatter) is TerminalFormatter
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert formatter.kwargs == {"format_options": format_options}
    assert formatter.format_options is format_options


def test_color_formatter_uses_256_color_formatter_for_explicit_style():
    format_options = {"body": True}
    style_class = ColorFormatter.get_style_class("monokai")

    formatter = ColorFormatter(
        env=SimpleNamespace(colors=256),
        explicit_json=False,
        color_scheme="monokai",
        format_options=format_options,
    )

    assert formatter.enabled is True
    assert formatter.explicit_json is False
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert formatter.formatter.style is style_class
    assert formatter.kwargs == {"format_options": format_options}
    assert formatter.format_options is format_options
