# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

from sty import Register, Style
from sty.rendertype import RenderType


class FakeRule(RenderType):
    def __init__(self, x):
        self.args = [x]


def _make_register_with_style():
    reg = Register()
    reg.renderfuncs[FakeRule] = lambda x: f"<{x}>"
    reg.red = Style(FakeRule(1))
    return reg


def test_unmute_rerenders_style_attributes():
    reg = _make_register_with_style()
    assert reg.is_muted is False
    assert str(reg.red) == "<1>"
    assert reg.red == "<1>"

    reg.mute()
    assert reg.is_muted is True
    assert str(reg.red) == ""

    assert reg.unmute() is None
    assert reg.is_muted is False
    assert str(reg.red) == "<1>"
    assert len(reg.red.rules) == 1
    assert reg.red.rules[0].args == [1]


def test_unmute_without_style_attributes():
    reg = Register()
    reg.mute()
    assert reg.is_muted is True
    assert reg.unmute() is None
    assert reg.is_muted is False


def test_unmute_is_idempotent_and_preserves_non_style_attributes():
    reg = _make_register_with_style()
    reg.plain = "not a style"
    reg.unmute()
    assert reg.is_muted is False
    assert str(reg.red) == "<1>"
    assert reg.plain == "not a style"

    reg.unmute()
    assert str(reg.red) == "<1>"
    assert reg.plain == "not a style"


def test_unmute_handles_class_level_style_attributes():
    class CustomRegister(Register):
        pass

    CustomRegister.blue = Style(FakeRule(4))
    try:
        reg = CustomRegister()
        reg.renderfuncs[FakeRule] = lambda x: f"<{x}>"
        reg.mute()
        assert reg.is_muted is True
        assert str(reg.blue) == ""
        reg.unmute()
        assert reg.is_muted is False
        assert str(reg.blue) == "<4>"
    finally:
        del CustomRegister.blue
