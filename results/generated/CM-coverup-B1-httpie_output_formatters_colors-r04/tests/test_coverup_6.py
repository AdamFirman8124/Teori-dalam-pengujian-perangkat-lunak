# file: project/httpie/output/formatters/colors.py:101-106
# asked: {"lines": [103, 104, 105, 106], "branches": []}
# gained: {"lines": [103, 104, 105, 106], "branches": []}

import pygments.styles
import pygments.style
from pygments.util import ClassNotFound

import httpie.output.formatters.colors as colors_module
from httpie.output.formatters.colors import ColorFormatter, Solarized256Style


def test_get_style_class_returns_pygments_style_for_valid_scheme(monkeypatch):
    """A known color scheme name resolves to the corresponding Pygments style class."""
    monkeypatch.setattr(
        pygments.styles,
        'get_style_by_name',
        lambda name: Solarized256Style if name == 'solarized' else _FakeStyle,
        raising=True,
    )

    result = ColorFormatter.get_style_class('solarized')

    assert result is Solarized256Style
    assert issubclass(result, pygments.style.Style)


def test_get_style_class_falls_back_on_unknown_scheme(monkeypatch):
    """An unknown color scheme name triggers the ClassNotFound branch (lines 105-106)."""

    def raise_class_not_found(name):
        raise ClassNotFound(f"no lexer for {name!r}")

    monkeypatch.setattr(
        pygments.styles,
        'get_style_by_name',
        raise_class_not_found,
        raising=True,
    )

    result = ColorFormatter.get_style_class('definitely-not-a-style')

    assert result is Solarized256Style
    assert issubclass(result, pygments.style.Style)


class _FakeStyle(pygments.style.Style):
    pass
