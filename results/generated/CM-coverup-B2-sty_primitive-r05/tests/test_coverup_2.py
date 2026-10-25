# file: project/sty/primitive.py:142-156
# asked: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

from sty.primitive import Register, Style
from sty.rendertype import RenderType


def test_set_renderfunc_registers_function_without_styles():
    class CustomRenderType(RenderType):
        pass

    register = Register()

    def render(value):
        return f"<{value}>"

    register.set_renderfunc(CustomRenderType, render)

    assert register.renderfuncs[CustomRenderType] is render


def test_set_renderfunc_rerenders_existing_style_attributes():
    class CustomRenderType(RenderType):
        def __init__(self, value):
            self.args = [value]

    register = Register()

    def old_render(value):
        return f"old:{value}"

    def new_render(value):
        return f"new:{value}"

    register.renderfuncs[CustomRenderType] = old_render
    rule = CustomRenderType("content")
    register.example = Style(rule)

    assert register.example == "old:content"

    register.set_renderfunc(CustomRenderType, new_render)

    assert register.renderfuncs[CustomRenderType] is new_render
    assert isinstance(register.example, Style)
    assert register.example == "new:content"
    assert register.example.rules == (rule,)
