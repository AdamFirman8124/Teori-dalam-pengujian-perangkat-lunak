# file: project/sty/primitive.py:78-91
# asked: {"lines": [83], "branches": [[82, 83]]}
# gained: {"lines": [83], "branches": [[82, 83]]}

from sty.primitive import Register, Style


def test_setting_style_on_muted_register_clears_value_and_preserves_rules():
    register = Register()
    register.mute()

    rules = (object(), object())
    original = Style(*rules, value="rendered")
    register.example = original

    assert register.is_muted is True
    assert isinstance(register.example, Style)
    assert register.example == ""
    assert register.example.rules == rules
    assert register.example is not original
