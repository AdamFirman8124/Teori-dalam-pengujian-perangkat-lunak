# file: project/sty/primitive.py:158-168
# asked: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}
# gained: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}

from sty.primitive import Register, Style


def test_mute_sets_flag_and_clears_style_value():
    reg = Register()
    rule = object()
    original = Style(rule, value="\x1b[1m")
    object.__setattr__(reg, "my_style", original)

    assert reg.is_muted is False

    reg.mute()

    assert reg.is_muted is True
    muted = reg.my_style
    assert isinstance(muted, Style)
    assert str(muted) == ""
    assert muted.rules == (rule,)
    # the original Style object must not be mutated in place
    assert str(original) == "\x1b[1m"


def test_mute_clears_all_style_attributes_and_keeps_others():
    reg = Register()
    rule = object()
    object.__setattr__(reg, "plain", 42)
    object.__setattr__(reg, "style_a", Style(value="a"))
    object.__setattr__(reg, "style_b", Style(rule, value="b"))

    reg.mute()

    assert reg.is_muted is True
    assert reg.plain == 42
    assert isinstance(reg.style_a, Style)
    assert isinstance(reg.style_b, Style)
    assert str(reg.style_a) == ""
    assert str(reg.style_b) == ""
    assert reg.style_a.rules == ()
    assert reg.style_b.rules == (rule,)


def test_mute_is_idempotent_and_blocks_new_style_rendering():
    reg = Register()
    object.__setattr__(reg, "style_a", Style(value="a"))

    reg.mute()
    reg.mute()

    assert reg.is_muted is True
    assert str(reg.style_a) == ""

    # assigning a new Style while muted must store an empty value
    reg.style_new = Style(object(), value="rendered")

    assert isinstance(reg.style_new, Style)
    assert str(reg.style_new) == ""
    assert len(reg.style_new.rules) == 1
