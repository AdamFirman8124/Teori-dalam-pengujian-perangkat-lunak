# file: project/sty/primitive.py:142-156
# asked: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

from sty import Register, Style
from sty.rendertype import RenderType


class DummyRule(RenderType):
    def __init__(self, val=None):
        self.val = val
        self.args = [val] if val is not None else []


def test_set_renderfunc_updates_style_attributes():
    reg = Register()

    rule = DummyRule("rule")
    style = Style(rule, value="original")
    object.__setattr__(reg, "mystyle", style)
    assert reg.mystyle == "original"

    calls = []

    def render_func(*args):
        calls.append(args)
        return "<rendered>"

    reg.set_renderfunc(DummyRule, render_func)

    # line 150: new renderfunc saved in register
    assert reg.renderfuncs == {DummyRule: render_func}
    # lines 153-156: Style attribute found and re-set via __setattr__,
    # which re-renders it with the new renderfunc
    assert calls == [("rule",)]
    assert isinstance(reg.mystyle, Style)
    assert reg.mystyle == "<rendered>"
    assert reg.mystyle.rules == (rule,)


def test_set_renderfunc_replaces_existing_func_and_skips_non_style_attrs():
    reg = Register()
    reg.plain = "not-a-style"

    def first_func(*args):
        return "first"

    def second_func(*args):
        return "second"

    reg.set_renderfunc(DummyRule, first_func)
    assert reg.renderfuncs[DummyRule] is first_func

    # calling again with same rendertype replaces the entry (line 150)
    reg.set_renderfunc(DummyRule, second_func)
    assert reg.renderfuncs[DummyRule] is second_func
    assert len(reg.renderfuncs) == 1

    # False branch of isinstance check: non-Style attributes untouched
    assert reg.plain == "not-a-style"
    assert not isinstance(reg.plain, Style)
