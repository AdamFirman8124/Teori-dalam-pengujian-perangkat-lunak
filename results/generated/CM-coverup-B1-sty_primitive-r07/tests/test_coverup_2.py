# file: project/sty/primitive.py:142-156
# asked: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

from sty.primitive import Register, Style
from sty.rendertype import RenderType
import sty.primitive as prim


def test_set_renderfunc_rerenders_single_style(monkeypatch):
    calls = []

    def fake_render(renderfuncs, rules):
        calls.append((dict(renderfuncs), tuple(rules)))
        return ("fake-rendered-%d" % len(calls), tuple(rules))

    monkeypatch.setattr(prim, "_render_rules", fake_render)

    class DummyRender(RenderType):
        pass

    def new_func(rule):
        return "NEW"

    reg = Register()
    marker = object()
    reg.sample = Style(marker, value="orig")

    assert isinstance(reg.sample, Style)
    assert marker in reg.sample.rules
    n0 = len(calls)
    assert n0 == 1

    reg.set_renderfunc(DummyRender, new_func)

    # postcondition: renderfunc stored
    assert reg.renderfuncs[DummyRender] is new_func
    # postcondition: existing Style was re-set (re-rendered) once
    assert len(calls) == n0 + 1
    # postcondition: re-render saw the new renderfuncs dict
    assert calls[-1][0][DummyRender] is new_func
    # postcondition: rules preserved, value is re-rendered value
    assert isinstance(reg.sample, Style)
    assert marker in reg.sample.rules
    assert str(reg.sample) == "fake-rendered-%d" % len(calls)


def test_set_renderfunc_updates_multiple_styles_and_ignores_non_styles(monkeypatch):
    calls = []

    def fake_render(renderfuncs, rules):
        calls.append((dict(renderfuncs), tuple(rules)))
        return ("rendered-%d" % len(calls), tuple(rules))

    monkeypatch.setattr(prim, "_render_rules", fake_render)

    class RenderA(RenderType):
        pass

    def func_a(rule):
        return "A"

    reg = Register()
    r1 = object()
    r2 = object()
    reg.first = Style(r1, value="one")
    reg.second = Style(r2, value="two")
    reg.plain = "not-a-style"
    reg.number = 123

    assert isinstance(reg.first, Style)
    assert isinstance(reg.second, Style)
    n0 = len(calls)
    assert n0 == 2

    reg.set_renderfunc(RenderA, func_a)

    assert reg.renderfuncs[RenderA] is func_a
    # both Style attrs re-rendered, non-Style attrs did not trigger render
    assert len(calls) == n0 + 2
    assert calls[-2][0][RenderA] is func_a
    assert calls[-1][0][RenderA] is func_a
    # postconditions on values
    assert isinstance(reg.first, Style)
    assert isinstance(reg.second, Style)
    assert r1 in reg.first.rules
    assert r2 in reg.second.rules
    assert reg.plain == "not-a-style"
    assert reg.number == 123
    assert not isinstance(reg.plain, Style)


def test_set_renderfunc_no_styles_and_replace(monkeypatch):
    calls = []

    def fake_render(renderfuncs, rules):
        calls.append((dict(renderfuncs), tuple(rules)))
        return ("v%d" % len(calls), tuple(rules))

    monkeypatch.setattr(prim, "_render_rules", fake_render)

    class RenderB(RenderType):
        pass

    def func1(rule):
        return "one"

    def func2(rule):
        return "two"

    reg = Register()
    n0 = len(calls)
    assert n0 == 0

    # no Style attributes: loop executes but isinstance is always False
    reg.set_renderfunc(RenderB, func1)
    assert reg.renderfuncs[RenderB] is func1
    assert len(calls) == 0

    # replace renderfunc for same rendertype
    reg.marker = Style(value="x")
    n1 = len(calls)
    assert n1 == 1
    reg.set_renderfunc(RenderB, func2)
    assert reg.renderfuncs[RenderB] is func2
    assert len(calls) == n1 + 1
    assert calls[-1][0][RenderB] is func2
    assert isinstance(reg.marker, Style)
