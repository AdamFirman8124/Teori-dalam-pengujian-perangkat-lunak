# file: project/sty/primitive.py:158-168
# asked: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}
# gained: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}

from sty.primitive import Register, Style


def test_mute_sets_flag_and_blanks_style():
    reg = Register()
    original = Style(value="\x1b[31m")
    object.__setattr__(reg, "my_style", original)

    assert str(reg.my_style) == "\x1b[31m"
    assert isinstance(reg.my_style, Style)

    reg.mute()

    assert reg.is_muted is True
    assert isinstance(reg.my_style, Style)
    assert str(reg.my_style) == ""
    assert reg.my_style.rules == original.rules


def test_mute_preserves_non_style_attributes():
    reg = Register()
    object.__setattr__(reg, "my_style", Style(value="\x1b[32m"))
    reg.custom_number = 123
    reg.custom_string = "hello"

    reg.mute()

    assert reg.is_muted is True
    assert isinstance(reg.my_style, Style)
    assert str(reg.my_style) == ""
    assert reg.custom_number == 123
    assert reg.custom_string == "hello"
    assert reg.renderfuncs == {}
    assert reg.is_muted is True


def test_mute_empty_register_sets_flag():
    reg = Register()

    assert reg.is_muted is False

    reg.mute()

    assert reg.is_muted is True
    for attr_name in dir(reg):
        val = getattr(reg, attr_name)
        if isinstance(val, Style):
            assert str(val) == ""
