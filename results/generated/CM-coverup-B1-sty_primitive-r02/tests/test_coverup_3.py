# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

from sty.primitive import Register, Style


def test_unmute_rerenders_style_attributes_and_preserves_non_style_attributes():
    register = Register()
    marker = object()

    object.__setattr__(register, "example_style", Style(value="muted"))
    register.marker = marker
    register.is_muted = True

    register.unmute()

    assert register.is_muted is False
    assert isinstance(register.example_style, Style)
    assert register.example_style == ""
    assert register.example_style.rules == ()
    assert register.marker is marker
