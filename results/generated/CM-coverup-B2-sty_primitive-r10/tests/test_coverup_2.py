# file: project/sty/primitive.py:142-156
# asked: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

from typing import Callable

from sty import Register, Style
from sty.rendertype import RenderType


class _DummyRenderType(RenderType):
    args = []


def _first_func(*args) -> str:
    return "first:"


def _second_func(*args) -> str:
    return "second:"


def test_set_renderfunc_updates_renderfuncs_and_rerenders_style() -> None:
    reg = Register()
    rule = _DummyRenderType()

    # Register the renderfunc before creating a Style that uses the rule,
    # otherwise Register.__setattr__ raises KeyError in _render_rules.
    reg.set_renderfunc(_DummyRenderType, _first_func)
    assert reg.renderfuncs == {_DummyRenderType: _first_func}

    reg.mystyle = Style(rule)
    assert isinstance(reg.mystyle, Style)
    assert str(reg.mystyle) == "first:"
    assert reg.mystyle.rules == (rule,)

    # Lines 150-156: replacing the renderfunc re-sets Style attributes,
    # which re-renders them with the new function.
    reg.set_renderfunc(_DummyRenderType, _second_func)

    assert reg.renderfuncs == {_DummyRenderType: _second_func}
    assert isinstance(reg.mystyle, Style)
    assert str(reg.mystyle) == "second:"
    assert reg.mystyle.rules == (rule,)


def test_set_renderfunc_ignores_non_style_attributes() -> None:
    reg = Register()
    rule = _DummyRenderType()
    reg.set_renderfunc(_DummyRenderType, _first_func)

    reg.mystyle = Style(rule)
    reg.plain_attr = "not-a-style"
    assert str(reg.mystyle) == "first:"

    reg.set_renderfunc(_DummyRenderType, _second_func)

    assert reg.renderfuncs == {_DummyRenderType: _second_func}
    assert reg.plain_attr == "not-a-style"
    assert reg.is_muted is False
    assert isinstance(reg.mystyle, Style)
    assert str(reg.mystyle) == "second:"
    assert reg.mystyle.rules == (rule,)
