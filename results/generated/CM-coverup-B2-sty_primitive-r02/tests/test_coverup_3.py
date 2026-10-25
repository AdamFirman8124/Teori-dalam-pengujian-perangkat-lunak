# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

from sty.primitive import Register, Style
from sty.rendertype import RgbFg


def _make_register():
    reg = Register()
    reg.renderfuncs[RgbFg] = lambda *args: "\x1b[38;2;1;2;3m"
    reg.color = Style(RgbFg(1, 2, 3))
    return reg


def test_unmute_restores_rendered_style():
    reg = _make_register()
    assert isinstance(reg.color, Style)
    assert str(reg.color) == "\x1b[38;2;1;2;3m"

    reg.mute()
    assert reg.is_muted is True
    assert str(reg.color) == ""
    assert isinstance(reg.color, Style)

    reg.unmute()

    assert reg.is_muted is False
    assert isinstance(reg.color, Style)
    assert str(reg.color) == "\x1b[38;2;1;2;3m"
    assert len(reg.color.rules) == 1
    assert isinstance(reg.color.rules[0], RgbFg)


def test_unmute_is_idempotent_when_not_muted():
    reg = _make_register()
    assert reg.is_muted is False

    reg.unmute()
    assert reg.is_muted is False
    assert str(reg.color) == "\x1b[38;2;1;2;3m"

    reg.unmute()
    assert reg.is_muted is False
    assert str(reg.color) == "\x1b[38;2;1;2;3m"


def test_unmute_leaves_non_style_attributes_untouched():
    reg = _make_register()
    reg.plain = "hello"
    reg.number = 42

    reg.mute()
    assert reg.plain == "hello"
    assert reg.number == 42

    reg.unmute()

    assert reg.is_muted is False
    assert reg.plain == "hello"
    assert reg.number == 42
    assert str(reg.color) == "\x1b[38;2;1;2;3m"


def test_unmute_handles_style_rendering_to_empty_string():
    reg = Register()
    reg.renderfuncs[RgbFg] = lambda *args: ""
    reg.color = Style(RgbFg(4, 5, 6))
    assert str(reg.color) == ""

    reg.mute()
    assert str(reg.color) == ""

    reg.unmute()

    assert reg.is_muted is False
    assert isinstance(reg.color, Style)
    assert str(reg.color) == ""
    assert len(reg.color.rules) == 1
