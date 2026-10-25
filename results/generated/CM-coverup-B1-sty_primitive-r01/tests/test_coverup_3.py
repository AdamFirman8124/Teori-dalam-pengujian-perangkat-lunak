# file: project/sty/primitive.py:158-168
# asked: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}
# gained: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}

import pytest

from sty import Register, Style, Sgr


def test_mute_clears_style_attributes_and_sets_flag():
    reg = Register()
    # Bypass Register.__setattr__ so the style keeps a rendered value.
    object.__setattr__(reg, 'custom_style', Style(Sgr(1), value='\x1b[1m'))
    assert str(reg.custom_style) == '\x1b[1m'
    assert reg.is_muted is False

    reg.mute()

    assert reg.is_muted is True
    assert isinstance(reg.custom_style, Style)
    assert str(reg.custom_style) == ''
    # Sgr instances do not implement __eq__, so compare structurally.
    assert len(reg.custom_style.rules) == 1
    assert isinstance(reg.custom_style.rules[0], Sgr)


def test_mute_without_style_attributes_only_sets_flag():
    reg = Register()
    reg.plain_value = 42

    reg.mute()

    assert reg.is_muted is True
    assert reg.plain_value == 42
