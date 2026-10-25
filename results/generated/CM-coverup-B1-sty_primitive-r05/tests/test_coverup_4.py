# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

from sty import Register, Style
from sty.rendertype import RgbFg, Sgr


def _make_register_with_style():
    reg = Register()
    reg.renderfuncs[RgbFg] = lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m"
    reg.renderfuncs[Sgr] = lambda *attrs: f"\x1b[{';'.join(map(str, attrs))}m"
    reg.orange = Style(RgbFg(1, 5, 10), Sgr(1))
    return reg


def test_unmute_rerenders_style_attributes():
    reg = _make_register_with_style()
    original_rules = reg.orange.rules
    assert reg.is_muted is False
    assert isinstance(reg.orange, Style)
    assert str(reg.orange) == "\x1b[38;2;1;5;10m\x1b[1m"
    assert reg.orange == "\x1b[38;2;1;5;10m\x1b[1m"

    reg.mute()
    assert reg.is_muted is True
    assert str(reg.orange) == ""

    assert reg.unmute() is None
    assert reg.is_muted is False
    assert isinstance(reg.orange, Style)
    assert str(reg.orange) == "\x1b[38;2;1;5;10m\x1b[1m"
    assert reg.orange.rules == original_rules


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
    assert str(reg.orange) == "\x1b[38;2;1;5;10m\x1b[1m"
    assert reg.plain == "not a style"

    reg.unmute()
    assert str(reg.orange) == "\x1b[38;2;1;5;10m\x1b[1m"
    assert reg.plain == "not a style"


def test_unmute_handles_class_level_style_attributes():
    class CustomRegister(Register):
        pass

    CustomRegister.blue = Style(RgbFg(0, 0, 255))
    try:
        reg = CustomRegister()
        reg.renderfuncs[RgbFg] = lambda r, g, b: f"\x1b[38;2;{r};{g};{b}m"
        reg.mute()
        assert reg.is_muted is True
        assert str(reg.blue) == ""
        reg.unmute()
        assert reg.is_muted is False
        assert str(reg.blue) == "\x1b[38;2;0;0;255m"
    finally:
        del CustomRegister.blue
