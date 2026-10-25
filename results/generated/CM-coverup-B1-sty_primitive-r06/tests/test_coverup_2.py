# file: project/sty/primitive.py:142-156
# asked: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

from typing import Callable

from sty import Register, Style
from sty.rendertype import RenderType


class _DummyRenderType(RenderType):
    """Minimal concrete RenderType used only for testing."""

    args: list = []


class _OtherRenderType(RenderType):
    args: list = []


def _render_a() -> str:
    return "\x1b[1m"


def _render_b() -> str:
    return "\x1b[2m"


class _TestRegister(Register):
    """Register subclass isolated from the global registers."""

    def __init__(self) -> None:
        super().__init__()


def test_set_renderfunc_updates_renderfuncs_and_rerenders_styles() -> None:
    reg = _TestRegister()

    # Precondition: no renderfuncs registered yet.
    assert reg.renderfuncs == {}

    # Line 150 + lines 153-156 with no Style attributes present yet.
    reg.set_renderfunc(_DummyRenderType, _render_a)
    assert reg.renderfuncs == {_DummyRenderType: _render_a}

    # Now create a Style attribute; it renders with the registered func.
    reg.mystyle = Style(_DummyRenderType(), value="original")
    assert isinstance(reg.mystyle, Style)
    assert reg.mystyle == "\x1b[1m"
    assert len(reg.mystyle.rules) == 1
    assert isinstance(reg.mystyle.rules[0], _DummyRenderType)

    # Lines 153-156: the Style attribute is re-set and re-rendered.
    reg.set_renderfunc(_DummyRenderType, _render_b)
    assert reg.renderfuncs == {_DummyRenderType: _render_b}
    assert isinstance(reg.mystyle, Style)
    assert reg.mystyle == "\x1b[2m"
    assert len(reg.mystyle.rules) == 1
    assert isinstance(reg.mystyle.rules[0], _DummyRenderType)

    # Adding a second rendertype keeps the first one and re-renders again.
    reg.set_renderfunc(_OtherRenderType, _render_a)
    assert reg.renderfuncs == {
        _DummyRenderType: _render_b,
        _OtherRenderType: _render_a,
    }
    assert reg.mystyle == "\x1b[2m"


def test_set_renderfunc_leaves_non_style_attributes_untouched() -> None:
    reg = _TestRegister()
    reg.set_renderfunc(_DummyRenderType, _render_a)
    reg.mystyle = Style(_DummyRenderType(), value="original")
    reg.plain_attr = "not-a-style"  # type: ignore[assignment]

    reg.set_renderfunc(_DummyRenderType, _render_b)

    # Non-Style attributes are skipped by the isinstance check on line 155.
    assert reg.plain_attr == "not-a-style"
    assert reg.renderfuncs == {_DummyRenderType: _render_b}
    assert isinstance(reg.mystyle, Style)
    assert reg.mystyle == "\x1b[2m"
