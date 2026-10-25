# file: project/sty/primitive.py:78-91
# asked: {"lines": [83], "branches": [[82, 83]]}
# gained: {"lines": [83], "branches": [[82, 83]]}

from sty.primitive import Register, Style


def test_register_setattr_muted_style_empty_value():
    reg = Register()
    reg.mute()
    assert reg.is_muted is True

    original = Style(value="rendered-output")
    reg.my_attr = original

    stored = object.__getattribute__(reg, "my_attr")
    assert isinstance(stored, Style)
    assert str(stored) == ""
    assert stored == ""
    assert stored.rules == original.rules


def test_register_setattr_muted_style_preserves_rules():
    reg = Register()
    reg.mute()
    assert reg.is_muted is True

    dummy_rule_one = object()
    dummy_rule_two = object()
    original = Style(dummy_rule_one, dummy_rule_two, value="some-rendered")

    reg.custom_style = original

    stored = object.__getattribute__(reg, "custom_style")
    assert isinstance(stored, Style)
    assert str(stored) == ""
    assert stored.rules == (dummy_rule_one, dummy_rule_two)
    # unmuted registers would store non-empty rendered string; muted must be empty
    assert stored.value if hasattr(stored, "value") else str(stored) == ""
