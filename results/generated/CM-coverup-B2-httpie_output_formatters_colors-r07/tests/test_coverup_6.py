# file: project/httpie/output/formatters/colors.py:101-106
# asked: {"lines": [103, 104, 105, 106], "branches": []}
# gained: {"lines": [103, 104, 105, 106], "branches": []}

import pygments.styles
from pygments.util import ClassNotFound

from httpie.output.formatters.colors import ColorFormatter, Solarized256Style


def test_get_style_class_valid_style_name():
    """A known pygments style name resolves via pygments (lines 103-104)."""
    style_class = ColorFormatter.get_style_class('monokai')
    assert style_class is pygments.styles.get_style_by_name('monokai')
    assert issubclass(style_class, pygments.style.Style)


def test_get_style_class_unknown_style_falls_back(monkeypatch):
    """An unknown style name raises ClassNotFound internally and
    falls back to Solarized256Style (lines 105-106)."""

    def raise_class_not_found(name):
        raise ClassNotFound(name)

    monkeypatch.setattr(
        pygments.styles, 'get_style_by_name', raise_class_not_found
    )
    style_class = ColorFormatter.get_style_class('definitely-not-a-style')
    assert style_class is Solarized256Style
    assert issubclass(style_class, pygments.style.Style)
