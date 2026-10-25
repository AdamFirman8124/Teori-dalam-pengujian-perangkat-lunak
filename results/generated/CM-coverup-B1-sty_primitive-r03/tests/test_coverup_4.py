# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

from sty.primitive import Register, Style


def test_unmute_reassigns_style_attributes_and_clears_muted_flag(monkeypatch):
    register = Register()
    register.example = Style()
    register.mute()

    assignments = []
    original_setattr = Register.__setattr__

    def tracking_setattr(self, name, value):
        if self is register:
            assignments.append((name, value))
        return original_setattr(self, name, value)

    monkeypatch.setattr(Register, "__setattr__", tracking_setattr)

    register.unmute()

    assert register.is_muted is False
    assert isinstance(register.example, Style)
    assert any(name == "example" and isinstance(value, Style)
               for name, value in assignments)
