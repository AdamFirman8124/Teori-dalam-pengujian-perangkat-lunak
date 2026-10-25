# file: project/sty/primitive.py:158-168
# asked: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}
# gained: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}

from sty.primitive import Register, Style


def test_mute_plain_register_without_styles():
    r = Register()
    assert r.is_muted is False

    r.mute()

    assert r.is_muted is True
    # non-Style state must be preserved
    assert r.renderfuncs == {}
    assert r.is_muted is True


def test_mute_clears_style_attributes():
    r = Register()
    original = Style(value="\x1b[31m")
    other = Style(value="\x1b[32m")
    assert isinstance(original, Style)
    assert str(original) == "\x1b[31m"

    # Bypass Register.__setattr__ rendering so we have non-empty
    # Style values even with empty renderfuncs.
    object.__setattr__(r, "my_red", original)
    object.__setattr__(r, "my_green", other)
    assert r.my_red == "\x1b[31m"
    assert r.my_green == "\x1b[32m"

    r.mute()

    # postconditions: muted flag set and every Style re-set to empty value
    assert r.is_muted is True
    assert isinstance(r.my_red, Style)
    assert isinstance(r.my_green, Style)
    assert str(r.my_red) == ""
    assert str(r.my_green) == ""
    # rules are preserved by mute's Style(*value.rules, value='') path
    assert r.my_red.rules == original.rules
    assert r.my_green.rules == other.rules
