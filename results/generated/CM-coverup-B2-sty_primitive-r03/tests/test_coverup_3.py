# file: project/sty/primitive.py:158-168
# asked: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}
# gained: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}

from sty.primitive import Register, Style


def test_mute_rerenders_style_attributes_as_empty() -> None:
    register = Register()
    original_style = Style(value="visible")
    object.__setattr__(register, "custom_style", original_style)

    assert register.is_muted is False
    assert register.custom_style == "visible"

    register.mute()

    assert register.is_muted is True
    assert isinstance(register.custom_style, Style)
    assert register.custom_style == ""
    assert register.custom_style.rules == original_style.rules
