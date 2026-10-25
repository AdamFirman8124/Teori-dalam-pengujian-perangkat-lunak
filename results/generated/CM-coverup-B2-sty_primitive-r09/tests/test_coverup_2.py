# file: project/sty/primitive.py:142-156
# asked: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

from sty.primitive import Register, Style
from sty.rendertype import RenderType


def test_set_renderfunc_updates_existing_style_attributes():
    class CustomRenderType(RenderType):
        pass

    register = Register()
    old_renderfunc = lambda: "old"
    new_renderfunc = lambda: "new"

    register.set_renderfunc(CustomRenderType, old_renderfunc)
    register.accent = Style(CustomRenderType())

    assert isinstance(register.accent, Style)
    assert register.accent == "old"

    register.set_renderfunc(CustomRenderType, new_renderfunc)

    assert register.renderfuncs[CustomRenderType] is new_renderfunc
    assert isinstance(register.accent, Style)
    assert register.accent == "new"
