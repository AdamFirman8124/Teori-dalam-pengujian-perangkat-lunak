# file: project/sty/primitive.py:142-156
# asked: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

"""Tests covering Register.set_renderfunc in sty/primitive.py (lines 150-156).

Note: Register.__setattr__ renders Style attributes via _render_rules, which
looks up renderfuncs[type(rule)] and invokes it as f1(*rule.args). Therefore
the fake render functions must accept the rule's unpacked args.

All state mutated by set_renderfunc lives on the instance (renderfuncs is
created in Register.__init__), so using fresh Register instances per test
keeps the global sty registers (fg/bg/ef/rs) untouched and no monkeypatching
or extra cleanup is required.
"""

from sty.primitive import Register, Style
from sty.rendertype import RenderType


class _DummyRenderType(RenderType):
    """Custom render type used as a renderfuncs key."""

    def __init__(self, *args):
        # Shadow the shared class-level 'args' list with per-instance args.
        self.args = args


class _OtherRenderType(RenderType):
    """A second custom render type."""

    def __init__(self, *args):
        self.args = args


def _render_one(*args):
    return "<rendered-one>"


def _render_two(*args):
    return "<rendered-two>"


def test_set_renderfunc_registers_func_and_rerenders_style_attributes():
    # Phase 1: register renderfuncs while no Style attribute exists yet.
    # The update loop runs, but isinstance(val, Style) is False for every
    # attribute, so only lines 150-155 (False branch) execute here.
    reg = Register()
    reg.set_renderfunc(_DummyRenderType, _render_one)
    reg.set_renderfunc(_OtherRenderType, _render_one)
    assert reg.renderfuncs == {
        _DummyRenderType: _render_one,
        _OtherRenderType: _render_one,
    }

    # Phase 2: attach a Style attribute; Register.__setattr__ renders it
    # with the currently registered renderfunc (_render_one).
    rule = _DummyRenderType(1, 2)
    reg.mystyle = Style(rule)
    assert isinstance(reg.mystyle, Style)
    assert str(reg.mystyle) == "<rendered-one>"
    assert rule in reg.mystyle.rules

    # A non-Style attribute that must survive the update loop untouched.
    reg.plain = "untouched"
    assert reg.plain == "untouched"

    # Phase 3: replace the renderfunc for _DummyRenderType. The already
    # existing Style attribute must now be re-rendered with the new
    # function (this executes the isinstance-True branch, line 156).
    style_before = reg.mystyle
    reg.set_renderfunc(_DummyRenderType, _render_two)

    assert reg.renderfuncs == {
        _DummyRenderType: _render_two,
        _OtherRenderType: _render_one,
    }
    assert reg.mystyle is not style_before  # setattr re-created the Style.
    assert isinstance(reg.mystyle, Style)
    assert str(reg.mystyle) == "<rendered-two>"
    assert rule in reg.mystyle.rules
    assert reg.plain == "untouched"


def test_set_renderfunc_without_style_attributes():
    """set_renderfunc also works when the register holds no Style attrs."""
    reg = Register()
    reg.set_renderfunc(_DummyRenderType, _render_one)

    assert reg.renderfuncs == {_DummyRenderType: _render_one}
    # Nothing else on the register was modified by the update loop.
    assert reg.is_muted is False
