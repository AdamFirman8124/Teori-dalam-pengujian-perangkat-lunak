# file: project/httpie/output/formatters/colors.py:101-106
# asked: {"lines": [103, 104, 105, 106], "branches": []}
# gained: {"lines": [103, 104, 105, 106], "branches": []}

import pygments.styles
import pytest
from pygments.util import ClassNotFound

from httpie.output.formatters.colors import ColorFormatter, Solarized256Style


def test_get_style_class_returns_requested_style():
    style = ColorFormatter.get_style_class('default')
    assert style is pygments.styles.get_style_by_name('default')
    assert style is not Solarized256Style


def test_get_style_class_falls_back_to_solarized_on_class_not_found(monkeypatch):
    calls = []

    def fake_get_style_by_name(name):
        calls.append(name)
        raise ClassNotFound(f'no style named {name!r}')

    monkeypatch.setattr(pygments.styles, 'get_style_by_name', fake_get_style_by_name)

    style = ColorFormatter.get_style_class('definitely-not-a-real-style')

    assert style is Solarized256Style
    assert calls == ['definitely-not-a-real-style']


def test_get_style_class_falls_back_for_unknown_scheme_name():
    # Exercises the real pygments lookup raising ClassNotFound (no patching).
    style = ColorFormatter.get_style_class('definitely-not-a-real-style')
    assert style is Solarized256Style
