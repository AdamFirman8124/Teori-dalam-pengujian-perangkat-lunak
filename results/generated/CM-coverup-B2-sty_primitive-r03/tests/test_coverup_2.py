# file: project/sty/primitive.py:142-156
# asked: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

from typing import Callable

import pytest

from sty import Register, Style
from sty.rendertype import RenderType


class _DummyRenderType(RenderType):
    """Minimal concrete RenderType used only for testing."""


def _dummy_render(*args) -> str:
    # RenderType.args defaults to [], so render funcs are called with no args.
    return "<dummy>"


def _other_render(*args) -> str:
    return "<other>"


class _TestRegister(Register):
    """Register subclass with one Style attribute, isolated from global registers."""

    def __init__(self) -> None:
        super().__init__()
        # A renderfunc must exist before a Style attribute can be set, because
        # Register.__setattr__ renders the rules immediately.
        self.set_renderfunc(_DummyRenderType, _dummy_render)
        self.mystyle = Style(_DummyRenderType(), value="original")


def test_set_renderfunc_updates_renderfuncs_and_styles() -> None:
    reg = _TestRegister()
    original_rule = reg.mystyle.rules[0]

    # Precondition: the renderfunc registered in __init__ is in place.
    assert reg.renderfuncs == {_DummyRenderType: _dummy_render}
    assert isinstance(reg.mystyle, Style)
    assert reg.mystyle == "<dummy>"

    # Line 150: renderfuncs dict is updated with the new func.
    reg.set_renderfunc(_DummyRenderType, _other_render)
    assert reg.renderfuncs == {_DummyRenderType: _other_render}

    # Lines 153-156: the Style attribute was re-set (re-rendered) via setattr,
    # so it now reflects the new renderfunc.
    assert isinstance(reg.mystyle, Style)
    assert isinstance(reg.mystyle, str)
    assert reg.mystyle == "<other>"

    # The rules of the style are preserved through the re-rendering: the very
    # same rule object (identity) is carried over, and its type is unchanged.
    assert len(reg.mystyle.rules) == 1
    assert reg.mystyle.rules[0] is original_rule
    assert isinstance(reg.mystyle.rules[0], _DummyRenderType)

    # Replacing the func for the same rendertype works repeatedly (update, not add).
    reg.set_renderfunc(_DummyRenderType, _dummy_render)
    assert reg.renderfuncs == {_DummyRenderType: _dummy_render}
    assert reg.mystyle == "<dummy>"
    assert isinstance(reg.mystyle, Style)


def test_set_renderfunc_ignores_non_style_attributes() -> None:
    reg = _TestRegister()
    reg.plain_attr = "not-a-style"  # type: ignore[assignment]

    reg.set_renderfunc(_DummyRenderType, _other_render)

    # Non-Style attributes are untouched by the re-set loop (line 155 is False).
    assert reg.plain_attr == "not-a-style"
    assert reg.renderfuncs == {_DummyRenderType: _other_render}
    assert isinstance(reg.mystyle, Style)
    assert reg.mystyle == "<other>"
