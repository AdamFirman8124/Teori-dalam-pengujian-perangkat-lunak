# file: project/httpie/output/formatters/colors.py:101-106
# asked: {"lines": [103, 104, 105, 106], "branches": []}
# gained: {"lines": [103, 104, 105, 106], "branches": []}

import pygments.styles
import pygments.style
import pytest
from pygments.util import ClassNotFound

from httpie.output.formatters.colors import ColorFormatter, Solarized256Style


def test_get_style_class_valid_style():
    """A valid pygments style name returns the corresponding style class."""
    style_class = ColorFormatter.get_style_class('monokai')
    expected = pygments.styles.get_style_by_name('monokai')
    assert style_class is expected
    assert issubclass(style_class, pygments.style.Style)


def test_get_style_class_invalid_style_falls_back_to_solarized(monkeypatch):
    """An unknown style name triggers ClassNotFound and returns Solarized256Style."""
    calls = []

    def fake_get_style_by_name(name):
        calls.append(name)
        raise ClassNotFound(f'no lexer for {name!r}')

    monkeypatch.setattr(
        pygments.styles, 'get_style_by_name', fake_get_style_by_name
    )

    style_class = ColorFormatter.get_style_class('definitely-not-a-style')

    assert calls == ['definitely-not-a-style']
    assert style_class is Solarized256Style
    assert issubclass(style_class, pygments.style.Style)
