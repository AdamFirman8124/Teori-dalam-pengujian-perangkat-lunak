# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

import pytest

from sty import Style, Sgr, RgbFg
from sty.register import FgRegister


def test_unmute_restores_style_attribute_values():
    reg = FgRegister()
    reg.my_color = Style(RgbFg(255, 0, 0), Sgr(1))
    expected = str(reg.my_color)
    assert expected != ""
    assert isinstance(reg.my_color, Style)

    reg.mute()
    assert reg.is_muted is True
    assert str(reg.my_color) == ""

    reg.unmute()

    assert reg.is_muted is False
    assert isinstance(reg.my_color, Style)
    assert str(reg.my_color) == expected
    assert len(reg.my_color.rules) == 2


def test_unmute_without_any_style_attributes():
    reg = FgRegister()
    reg.plain = "not a style"
    reg.number = 42

    reg.mute()
    assert reg.is_muted is True

    reg.unmute()

    assert reg.is_muted is False
    assert reg.plain == "not a style"
    assert reg.number == 42


def test_unmute_is_idempotent_and_keeps_non_style_attributes():
    reg = FgRegister()
    reg.my_blue = Style(RgbFg(0, 0, 255))
    reg.label = "keep me"
    expected = str(reg.my_blue)

    reg.mute()
    reg.unmute()
    reg.unmute()

    assert reg.is_muted is False
    assert str(reg.my_blue) == expected
    assert reg.label == "keep me"


def test_unmute_restores_multiple_styles_and_builtin_attributes():
    reg = FgRegister()
    reg.a = Style(Sgr(1))
    reg.b = Style(RgbFg(1, 2, 3))
    expected_a = str(reg.a)
    expected_b = str(reg.b)
    expected_red = str(reg.red)

    reg.mute()
    assert str(reg.a) == ""
    assert str(reg.b) == ""
    assert str(reg.red) == ""

    reg.unmute()

    assert str(reg.a) == expected_a
    assert str(reg.b) == expected_b
    assert str(reg.red) == expected_red
    assert reg.is_muted is False
