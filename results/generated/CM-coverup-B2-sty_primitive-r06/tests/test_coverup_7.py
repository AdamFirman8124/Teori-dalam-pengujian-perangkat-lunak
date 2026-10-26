# file: project/sty/primitive.py:78-91
# asked: {"lines": [83], "branches": [[82, 83]]}
# gained: {"lines": [83], "branches": [[82, 83]]}

from sty.primitive import Register, Style


def test_assigning_style_to_muted_register_preserves_rules_but_renders_empty():
    register = Register()
    rule = object()
    source_style = Style(rule, value="visible")

    register.mute()
    try:
        register.muted_style = source_style

        assert isinstance(register.muted_style, Style)
        assert register.muted_style == ""
        assert register.muted_style.rules == (rule,)
        assert register.muted_style is not source_style
    finally:
        if hasattr(register, "muted_style"):
            delattr(register, "muted_style")
        register.unmute()

    assert register.is_muted is False
