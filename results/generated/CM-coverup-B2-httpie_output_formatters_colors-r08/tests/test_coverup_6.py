# file: project/httpie/output/formatters/colors.py:101-106
# asked: {"lines": [103, 104, 105, 106], "branches": []}
# gained: {"lines": [103, 104, 105, 106], "branches": []}

import pygments.styles
from pygments.util import ClassNotFound

from httpie.output.formatters.colors import ColorFormatter, Solarized256Style


def test_get_style_class_returns_requested_style():
    expected = pygments.styles.get_style_by_name("monokai")
    result = ColorFormatter.get_style_class("monokai")
    assert result is expected


def test_get_style_class_fallback_on_unknown_scheme():
    result = ColorFormatter.get_style_class("definitely-not-a-pygments-style-xyz")
    assert result is Solarized256Style


def test_get_style_class_fallback_on_class_not_found(monkeypatch):
    def fake_get_style_by_name(name):
        raise ClassNotFound(f"No style found for {name!r}")

    monkeypatch.setattr(pygments.styles, "get_style_by_name", fake_get_style_by_name)
    result = ColorFormatter.get_style_class("anything")
    assert result is Solarized256Style
