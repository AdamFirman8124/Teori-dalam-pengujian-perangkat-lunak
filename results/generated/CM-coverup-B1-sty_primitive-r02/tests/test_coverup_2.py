# file: project/sty/primitive.py:158-168
# asked: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}
# gained: {"lines": [163, 165, 166, 167, 168], "branches": [[165, 0], [165, 166], [167, 165], [167, 168]]}

from sty.primitive import Register, Style


def test_register_mute_mutes_styles_and_preserves_other_attributes():
    register = Register()
    rule = Style(value="rule")
    visible_style = Style(rule, value="visible")

    object.__setattr__(register, "accent", visible_style)
    register.label = "unchanged"

    register.mute()

    assert register.is_muted is True
    assert isinstance(register.accent, Style)
    assert register.accent == ""
    assert register.accent.rules == (rule,)
    assert register.label == "unchanged"
