# file: project/sty/primitive.py:78-91
# asked: {"lines": [83], "branches": [[82, 83]]}
# gained: {"lines": [83], "branches": [[82, 83]]}

from sty.primitive import Register, Style


def test_setting_style_on_muted_register_preserves_rules_without_rendering(monkeypatch):
    register = Register()
    rule = object()
    source_style = Style(rule, value="rendered")

    monkeypatch.setattr(register, "is_muted", True)
    register.example = source_style

    assert isinstance(register.example, Style)
    assert register.example == ""
    assert register.example.rules == (rule,)
    assert register.example is not source_style
    assert source_style == "rendered"
