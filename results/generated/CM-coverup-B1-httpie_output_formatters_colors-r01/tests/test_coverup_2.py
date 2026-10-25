# file: project/httpie/output/formatters/colors.py:46-72
# asked: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}
# gained: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}

import pytest
from pygments.formatters.terminal import TerminalFormatter
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.text import HttpLexer as PygmentsHttpLexer
from pygments.styles import get_style_by_name

from httpie.context import Environment
from httpie.output.formatters.colors import (
    AUTO_STYLE,
    ColorFormatter,
    SimplifiedHTTPLexer,
)


def test_color_formatter_is_disabled_when_environment_has_no_colors():
    format_options = {}
    formatter = ColorFormatter(
        env=Environment(colors=0),
        explicit_json=True,
        format_options=format_options,
    )

    assert formatter.enabled is False
    assert formatter.format_options is format_options
    assert not hasattr(formatter, "formatter")
    assert not hasattr(formatter, "http_lexer")
    assert not hasattr(formatter, "explicit_json")


@pytest.mark.parametrize(
    ("colors", "color_scheme"),
    [
        (256, AUTO_STYLE),
        (16, "monokai"),
    ],
)
def test_color_formatter_uses_basic_terminal_formatter(
    colors,
    color_scheme,
):
    formatter = ColorFormatter(
        env=Environment(colors=colors),
        explicit_json=True,
        color_scheme=color_scheme,
        format_options={},
    )

    assert formatter.enabled is True
    assert formatter.explicit_json is True
    assert type(formatter.formatter) is TerminalFormatter
    assert type(formatter.http_lexer) is PygmentsHttpLexer


def test_color_formatter_uses_256_color_formatter_for_named_style(
    monkeypatch,
):
    style_class = get_style_by_name("monokai")
    requested_schemes = []

    def get_style_class(color_scheme):
        requested_schemes.append(color_scheme)
        return style_class

    monkeypatch.setattr(
        ColorFormatter,
        "get_style_class",
        staticmethod(get_style_class),
    )

    formatter = ColorFormatter(
        env=Environment(colors=256),
        explicit_json=False,
        color_scheme="monokai",
        format_options={},
    )

    assert formatter.enabled is True
    assert formatter.explicit_json is False
    assert type(formatter.formatter) is Terminal256Formatter
    assert formatter.formatter.style is style_class
    assert type(formatter.http_lexer) is SimplifiedHTTPLexer
    assert requested_schemes == ["monokai"]
