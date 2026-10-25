# file: project/httpie/output/formatters/colors.py:101-106
# asked: {"lines": [103, 104, 105, 106], "branches": []}
# gained: {"lines": [103, 104, 105, 106], "branches": []}

import pygments.styles
from pygments.util import ClassNotFound

from httpie.output.formatters.colors import ColorFormatter, Solarized256Style


def test_get_style_class_known_style(monkeypatch):
    sentinel_style = object()

    def fake_get_style_by_name(name):
        assert name == 'monokai'
        return sentinel_style

    monkeypatch.setattr(
        pygments.styles, 'get_style_by_name', fake_get_style_by_name
    )

    style_class = ColorFormatter.get_style_class('monokai')

    assert style_class is sentinel_style


def test_get_style_class_unknown_style_falls_back(monkeypatch):
    def fake_get_style_by_name(name):
        assert name == 'no-such-style'
        raise ClassNotFound(f"no lexer for {name!r}")

    monkeypatch.setattr(
        pygments.styles, 'get_style_by_name', fake_get_style_by_name
    )

    style_class = ColorFormatter.get_style_class('no-such-style')

    assert style_class is Solarized256Style
