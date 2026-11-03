# file: project/sty/primitive.py:142-156
# asked: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

"""Tests for Register.set_renderfunc (sty/primitive.py, lines 150-156)."""

from sty import Register, Style
from sty.rendertype import RenderType


def test_set_renderfunc_stores_function_in_renderfuncs():
    """
    Covers line 150 and lines 153-155 (False branch of the isinstance check):
    calling set_renderfunc on a register that has no Style attributes must
    store the function under the given render type, and the rescan loop must
    leave non-Style attributes untouched.
    """

    class MyRenderType(RenderType):
        """Custom render type used as the key in the register's renderfuncs."""

    def render_func(*args, **kwargs) -> str:
        return "RENDERED"

    # A fresh instance keeps the test fully isolated: renderfuncs is created
    # per instance in Register.__init__, so no module-level register (fg, bg,
    # ...) and no class attribute is mutated, and the instance is garbage
    # collected when the test ends -- no monkeypatching is required.
    reg = Register()
    assert reg.renderfuncs == {}

    reg.set_renderfunc(MyRenderType, render_func)

    # Line 150: the render function was registered under the given type.
    assert reg.renderfuncs == {MyRenderType: render_func}
    # Lines 153-155: non-Style attributes are visited but left unchanged.
    assert reg.is_muted is False


def test_set_renderfunc_rerenders_existing_style_attributes():
    """
    Covers lines 153-155 (True branch of the isinstance check) and line 156:
    Style attributes found during the rescan are re-set, which re-renders
    them through Register.__setattr__ with the newly registered function.
    """

    class MyRenderType(RenderType):
        """Custom render type used as the key in the register's renderfuncs."""

    def render_func(*args, **kwargs) -> str:
        return "RENDERED"

    def replacement_func(*args, **kwargs) -> str:
        return "RE-RENDERED"

    reg = Register()

    # Register the first render function, then create a Style attribute; the
    # assignment is rendered through Register.__setattr__ using render_func.
    reg.set_renderfunc(MyRenderType, render_func)
    rule = MyRenderType()
    reg.my_style = Style(rule)
    assert isinstance(reg.my_style, Style)
    assert str(reg.my_style) == "RENDERED"
    assert reg.my_style.rules == (rule,)

    old_style = reg.my_style

    # Second call: the rescan loop now finds a Style attribute, so line 156
    # executes and re-renders it with the replacement function.
    reg.set_renderfunc(MyRenderType, replacement_func)

    assert reg.renderfuncs == {MyRenderType: replacement_func}
    assert reg.my_style is not old_style  # line 156 re-set the attribute
    assert isinstance(reg.my_style, Style)
    assert str(reg.my_style) == "RE-RENDERED"
    assert reg.my_style.rules == (rule,)
