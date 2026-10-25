# file: project/httpie/output/formatters/colors.py:101-106
# asked: {"lines": [103, 104, 105, 106], "branches": []}
# gained: {"lines": [103, 104, 105, 106], "branches": []}

import pygments.styles
from pygments.style import Style
from pygments.util import ClassNotFound

import httpie.output.formatters.colors as colors_module
from httpie.output.formatters.colors import ColorFormatter


def test_get_style_class_known_style(monkeypatch):
    sentinel_style = type("SentinelStyle", (Style,), {})

    def fake_get_style_by_name(name):
        assert name == "monokai"
        return sentinel_style

    monkeypatch.setattr(
        pygments.styles,
        "get_style_by_name",
        fake_get_style_by_name,
    )

    assert ColorFormatter.get_style_class("monokai") is sentinel_style


def test_get_style_class_unknown_style_falls_back(monkeypatch):
    def fake_get_style_by_name(name):
        assert name == "no-such-style"
        raise ClassNotFound(name)

    monkeypatch.setattr(
        pygments.styles,
        "get_style_by_name",
        fake_get_style_by_name,
    )

    assert (
        ColorFormatter.get_style_class("no-such-style")
        is colors_module.Solarized256Style
    )
