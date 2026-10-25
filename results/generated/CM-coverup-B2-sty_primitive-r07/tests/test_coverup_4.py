# file: project/sty/primitive.py:170-179
# asked: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}
# gained: {"lines": [174, 176, 177, 178, 179], "branches": [[176, 0], [176, 177], [178, 176], [178, 179]]}

from sty.primitive import Register, Style
from sty.rendertype import RenderType


def test_unmute_restores_muted_styles():
    class FakeRule(RenderType):
        def __init__(self, *args):
            self.args = list(args)

    def fake_render(x):
        return x

    reg = Register()
    reg.set_renderfunc(FakeRule, fake_render)
    reg.red = Style(FakeRule("red"), value="ignored")
    reg.blue = Style(FakeRule("blue"), value="ignored")

    assert reg.is_muted is False
    assert reg.red == "red"
    assert reg.blue == "blue"

    reg.mute()
    assert reg.is_muted is True
    assert reg.red == ""
    assert reg.blue == ""
    assert reg.red.rules[0].args == ["red"]

    reg.unmute()
    assert reg.is_muted is False
    assert reg.red == "red"
    assert reg.blue == "blue"
    assert reg.red.rules[0].args == ["red"]
    assert reg.blue.rules[0].args == ["blue"]


def test_unmute_when_already_unmuted_keeps_styles():
    class FakeRule(RenderType):
        def __init__(self, *args):
            self.args = list(args)

    def fake_render(x):
        return x

    reg = Register()
    reg.set_renderfunc(FakeRule, fake_render)
    reg.item = Style(FakeRule("kept"), value="ignored")

    assert reg.is_muted is False
    assert reg.item == "kept"

    reg.unmute()

    assert reg.is_muted is False
    assert isinstance(reg.item, Style)
    assert reg.item == "kept"
