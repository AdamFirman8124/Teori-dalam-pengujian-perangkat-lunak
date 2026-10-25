# file: project/httpie/output/formatters/colors.py:101-106
# asked: {"lines": [103, 104, 105, 106], "branches": []}
# gained: {"lines": [103, 104, 105, 106], "branches": []}

import pygments.style
from pygments.util import ClassNotFound

from httpie.output.formatters import colors


def test_get_style_class_returns_requested_pygments_style(monkeypatch):
    class RequestedStyle(pygments.style.Style):
        styles = {}

    calls = []

    def fake_get_style_by_name(color_scheme):
        calls.append(color_scheme)
        return RequestedStyle

    monkeypatch.setattr(
        colors.pygments.styles,
        "get_style_by_name",
        fake_get_style_by_name,
    )

    result = colors.ColorFormatter.get_style_class("custom-style")

    assert result is RequestedStyle
    assert calls == ["custom-style"]


def test_get_style_class_falls_back_to_solarized256_style(monkeypatch):
    calls = []

    def fake_get_style_by_name(color_scheme):
        calls.append(color_scheme)
        raise ClassNotFound(color_scheme)

    monkeypatch.setattr(
        colors.pygments.styles,
        "get_style_by_name",
        fake_get_style_by_name,
    )

    result = colors.ColorFormatter.get_style_class("missing-style")

    assert result is colors.Solarized256Style
    assert calls == ["missing-style"]
