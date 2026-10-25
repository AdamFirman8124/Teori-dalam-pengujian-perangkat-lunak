# file: project/httpie/output/formatters/colors.py:46-72
# asked: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}
# gained: {"lines": [53, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 70, 71, 72], "branches": [[55, 56], [55, 59], [61, 62], [61, 65]]}

from types import SimpleNamespace

from pygments.formatters.terminal import TerminalFormatter
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.text import HttpLexer as PygmentsHttpLexer
from pygments.style import Style
from pygments.token import Text

from httpie.output.formatters.colors import (
    AUTO_STYLE,
    ColorFormatter,
    SimplifiedHTTPLexer,
)


def test_color_formatter_is_disabled_when_colors_are_unavailable():
    formatter = ColorFormatter(
        env=SimpleNamespace(colors=0),
        format_options={},
    )

    assert formatter.enabled is False
    assert not hasattr(formatter, "formatter")
    assert not hasattr(formatter, "http_lexer")
    assert not hasattr(formatter, "explicit_json")


def test_auto_style_uses_standard_terminal_formatter():
    formatter = ColorFormatter(
        env=SimpleNamespace(colors=256),
        color_scheme=AUTO_STYLE,
        explicit_json=True,
        format_options={},
    )

    assert formatter.enabled is True
    assert formatter.explicit_json is True
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)
    assert not isinstance(formatter.formatter, Terminal256Formatter)


def test_non_auto_style_with_fewer_than_256_colors_uses_standard_formatter():
    formatter = ColorFormatter(
        env=SimpleNamespace(colors=8),
        color_scheme="custom-style",
        explicit_json=False,
        format_options={},
    )

    assert formatter.enabled is True
    assert formatter.explicit_json is False
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)
    assert not isinstance(formatter.formatter, Terminal256Formatter)


def test_non_auto_style_with_256_colors_uses_256_formatter(monkeypatch):
    class TestStyle(Style):
        styles = {Text: "#ffffff"}

    requested_schemes = []

    def fake_get_style_class(color_scheme):
        requested_schemes.append(color_scheme)
        return TestStyle

    monkeypatch.setattr(
        ColorFormatter,
        "get_style_class",
        staticmethod(fake_get_style_class),
    )

    formatter = ColorFormatter(
        env=SimpleNamespace(colors=256),
        color_scheme="custom-style",
        explicit_json=True,
        format_options={},
    )

    assert formatter.enabled is True
    assert formatter.explicit_json is True
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert requested_schemes == ["custom-style"]
