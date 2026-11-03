# file: project/sty/primitive.py:142-156
# asked: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

"""Coverage tests for sty.primitive.Register.set_renderfunc (lines 150-156).

All tests operate on fresh, locally created Register instances, so no global
sty state (e.g. the module-level fg/bg/ef/rs registers) is ever touched or
mutated.  Consequently no monkeypatching/teardown is required to avoid state
pollution between tests.
"""

from sty.primitive import Register, Style
from sty.rendertype import RenderType


class _MyRule(RenderType):
    """Custom render type used only within these tests."""

    def __init__(self, x: str) -> None:
        self.args = [x]


def test_set_renderfunc_saves_func_and_scans_attributes():
    """Lines 150-155: the func is stored and non-Style attributes are skipped."""
    reg = Register()

    def render_func(x):
        return f"<{x}>"

    reg.set_renderfunc(_MyRule, render_func)

    # Postcondition: the renderfunc was saved under the given rendertype.
    assert reg.renderfuncs == {_MyRule: render_func}


def test_set_renderfunc_replaces_func_and_rerenders_styles():
    """Lines 150-156: existing Style attributes are re-set (re-rendered)."""
    reg = Register()

    def old_render(x):
        return f"<old:{x}>"

    def new_render(x):
        return f"<new:{x}>"

    # First call: no Style attributes exist yet, so the loop inside
    # set_renderfunc finds nothing (False branch of the isinstance check).
    reg.set_renderfunc(_MyRule, old_render)
    assert reg.renderfuncs[_MyRule] is old_render

    # Assigning a Style attribute renders it with the currently registered
    # renderfunc (via Register.__setattr__ / _render_rules).
    rule = _MyRule("X")
    reg.red = Style(rule)
    assert reg.red == "<old:X>"
    assert isinstance(reg.red, Style)

    # Second call: the loop now finds the Style attribute and re-sets it,
    # which re-renders it with the newly registered renderfunc (line 156).
    reg.set_renderfunc(_MyRule, new_render)

    # Postconditions: the new func replaced the old one and the style
    # attribute was re-rendered through it, keeping its styling rule.
    assert reg.renderfuncs[_MyRule] is new_render
    assert reg.red == "<new:X>"
    assert isinstance(reg.red, Style)
    assert reg.red.rules == (rule,)


def test_set_renderfunc_on_muted_register_keeps_styles_empty():
    """Line 156 also runs for muted registers (styles stay rendered as '')."""
    reg = Register()
    reg.mute()
    assert reg.is_muted is True

    rule = _MyRule("X")
    reg.red = Style(rule)
    assert reg.red == ""

    def render_func(x):
        return f"<{x}>"

    reg.set_renderfunc(_MyRule, render_func)

    # Postconditions: the func was saved; the muted register keeps an empty
    # rendered value, but the styling rule itself is preserved.
    assert reg.renderfuncs[_MyRule] is render_func
    assert reg.red == ""
    assert reg.red.rules == (rule,)
