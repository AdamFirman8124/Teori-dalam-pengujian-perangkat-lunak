# file: project/sty/primitive.py:142-156
# asked: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

from sty.primitive import Register, Style
from sty.rendertype import RenderType


class ExampleRenderType(RenderType):
    def __init__(self, value):
        self.args = [value]


def test_set_renderfunc_replaces_renderer_and_rerenders_style_attributes():
    register = Register()
    register.renderfuncs[ExampleRenderType] = lambda value: f"old:{value}"
    register.label = "unchanged"
    register.accent = Style(ExampleRenderType("value"))

    assert register.accent == "old:value"

    new_renderfunc = lambda value: f"new:{value}"
    register.set_renderfunc(ExampleRenderType, new_renderfunc)

    assert register.renderfuncs[ExampleRenderType] is new_renderfunc
    assert isinstance(register.accent, Style)
    assert register.accent == "new:value"
    assert register.label == "unchanged"
    assert len(register.accent.rules) == 1
    assert isinstance(register.accent.rules[0], ExampleRenderType)
    assert register.accent.rules[0].args == ["value"]
