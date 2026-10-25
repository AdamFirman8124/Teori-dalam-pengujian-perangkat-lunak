# file: project/httpie/output/formatters/colors.py:101-106
# asked: {"lines": [103, 104, 105, 106], "branches": []}
# gained: {"lines": [103, 104, 105, 106], "branches": []}

import pygments.styles
from pygments.util import ClassNotFound

from httpie.output.formatters.colors import ColorFormatter, Solarized256Style


def test_get_style_class_returns_matching_style():
    style = ColorFormatter.get_style_class('monokai')
    assert style is pygments.styles.get_style_by_name('monokai')
    assert issubclass(style, pygments.style.Style)


def test_get_style_class_falls_back_on_class_not_found(monkeypatch):
    def raise_not_found(name):
        raise ClassNotFound(f'Could not find style {name!r}')

    monkeypatch.setattr(
        pygments.styles, 'get_style_by_name', raise_not_found
    )
    style = ColorFormatter.get_style_class('nonexistent-style')
    assert style is Solarized256Style
    assert issubclass(style, pygments.style.Style)
