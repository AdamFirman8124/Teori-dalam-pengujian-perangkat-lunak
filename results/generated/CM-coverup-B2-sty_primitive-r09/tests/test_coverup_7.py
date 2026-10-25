# file: project/sty/primitive.py:78-91
# asked: {"lines": [83], "branches": [[82, 83]]}
# gained: {"lines": [83], "branches": [[82, 83]]}

from sty.primitive import Register, Style


def test_assigning_style_to_muted_register_renders_empty_value():
    register = Register()
    register.mute()
    rule = object()
    original_style = Style(rule, value="original")

    register.example = original_style

    assert register.is_muted is True
    assert isinstance(register.example, Style)
    assert register.example == ""
    assert register.example.rules == (rule,)
    assert register.example is not original_style
