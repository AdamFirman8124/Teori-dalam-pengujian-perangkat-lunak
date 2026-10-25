# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

from sty.primitive import Register, Style


def test_unmute_restores_style_attributes_and_preserves_non_style_attributes():
    register = Register()
    register.is_muted = True

    muted_style = Style(value="muted")
    object.__setattr__(register, "custom_style", muted_style)
    register.non_style_attribute = "unchanged"

    register.unmute()

    assert register.is_muted is False
    assert isinstance(register.custom_style, Style)
    assert register.custom_style == ""
    assert register.custom_style is not muted_style
    assert register.non_style_attribute == "unchanged"
