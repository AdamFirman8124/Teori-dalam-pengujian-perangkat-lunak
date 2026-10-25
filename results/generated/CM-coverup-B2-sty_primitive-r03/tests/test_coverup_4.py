# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

import sty.primitive as primitive
from sty.primitive import Register, Style


def test_unmute_restores_registered_styles(monkeypatch):
    rendered_value = "\x1b[31m"

    def fake_render_rules(renderfuncs, rules):
        return rendered_value, rules

    monkeypatch.setattr(primitive, "_render_rules", fake_render_rules)

    register = Register()
    register.example = Style(value="initial")

    register.mute()
    assert register.is_muted is True
    assert isinstance(register.example, Style)
    assert str(register.example) == ""

    register.unmute()

    assert register.is_muted is False
    assert isinstance(register.example, Style)
    assert str(register.example) == rendered_value
