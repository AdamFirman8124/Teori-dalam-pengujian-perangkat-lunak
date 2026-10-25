# file: project/httpie/output/formatters/colors.py:101-106
# asked: {"lines": [103, 104, 105, 106], "branches": []}
# gained: {"lines": [103, 104, 105, 106], "branches": []}

import pygments.styles
from pygments.util import ClassNotFound

import httpie.output.formatters.colors as colors_module
from httpie.output.formatters.colors import ColorFormatter


def test_get_style_class_valid_scheme(monkeypatch):
    sentinel = object()

    def fake_get_style_by_name(name):
        assert name == 'monokai'
        return sentinel

    monkeypatch.setattr(
        pygments.styles, 'get_style_by_name', fake_get_style_by_name
    )

    result = ColorFormatter.get_style_class('monokai')

    assert result is sentinel


def test_get_style_class_invalid_scheme_falls_back(monkeypatch):
    def fake_get_style_by_name(name):
        raise ClassNotFound(name)

    monkeypatch.setattr(
        pygments.styles, 'get_style_by_name', fake_get_style_by_name
    )

    result = ColorFormatter.get_style_class('nonexistent-style')

    assert result is colors_module.Solarized256Style
