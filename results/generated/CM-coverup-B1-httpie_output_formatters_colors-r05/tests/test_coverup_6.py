# file: project/httpie/output/formatters/colors.py:101-106
# asked: {"lines": [103, 104, 105, 106], "branches": []}
# gained: {"lines": [103, 104, 105, 106], "branches": []}

from pygments.style import Style
from pygments.util import ClassNotFound

from httpie.output.formatters import colors


def test_get_style_class_returns_requested_style(monkeypatch):
    class ExpectedStyle(Style):
        styles = {}

    requested_schemes = []

    def get_style_by_name(color_scheme):
        requested_schemes.append(color_scheme)
        return ExpectedStyle

    monkeypatch.setattr(
        colors.pygments.styles,
        "get_style_by_name",
        get_style_by_name,
    )

    result = colors.ColorFormatter.get_style_class("custom")

    assert result is ExpectedStyle
    assert requested_schemes == ["custom"]


def test_get_style_class_falls_back_to_solarized(monkeypatch):
    requested_schemes = []

    def get_style_by_name(color_scheme):
        requested_schemes.append(color_scheme)
        raise ClassNotFound(color_scheme)

    monkeypatch.setattr(
        colors.pygments.styles,
        "get_style_by_name",
        get_style_by_name,
    )

    result = colors.ColorFormatter.get_style_class("missing")

    assert result is colors.Solarized256Style
    assert requested_schemes == ["missing"]
