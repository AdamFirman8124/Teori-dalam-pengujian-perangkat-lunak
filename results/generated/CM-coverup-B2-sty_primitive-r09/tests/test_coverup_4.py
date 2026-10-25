# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

from sty.primitive import Register, Style


def test_unmute_rerenders_style_attributes(monkeypatch):
    register = Register()
    original_style = Style(value="stale")
    object.__setattr__(register, "custom_style", original_style)
    object.__setattr__(register, "is_muted", True)

    assignments = []
    original_setattr = Register.__setattr__

    def tracking_setattr(self, name, value):
        assignments.append((name, value))
        return original_setattr(self, name, value)

    monkeypatch.setattr(Register, "__setattr__", tracking_setattr)

    register.unmute()

    assert register.is_muted is False
    assert ("custom_style", original_style) in assignments
    assert isinstance(register.custom_style, Style)
    assert register.custom_style == ""
