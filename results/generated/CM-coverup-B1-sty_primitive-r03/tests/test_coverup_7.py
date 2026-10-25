# file: project/sty/primitive.py:78-91
# asked: {"lines": [83], "branches": [[82, 83]]}
# gained: {"lines": [83], "branches": [[82, 83]]}

from sty.primitive import Register, Style


def test_setting_style_on_muted_register_renders_empty_value(monkeypatch):
    register = Register()
    register.mute()

    rule = object()
    source_style = Style(rule, value="visible")

    monkeypatch.setattr(register, "custom_style", source_style, raising=False)

    rendered_style = register.custom_style
    assert isinstance(rendered_style, Style)
    assert rendered_style == ""
    assert rendered_style.rules == (rule,)
    assert rendered_style is not source_style
    assert source_style == "visible"
