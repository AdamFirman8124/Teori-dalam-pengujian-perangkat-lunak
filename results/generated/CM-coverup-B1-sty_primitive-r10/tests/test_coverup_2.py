# file: project/sty/primitive.py:142-156
# asked: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

from typing import Callable

import pytest

from sty import Register, Style
from sty.rendertype import RenderType


class _DummyRenderType(RenderType):
    """Minimal concrete RenderType used only for testing."""


class _TestRegister(Register):
    """Register subclass with one Style attribute, isolated from global registers."""

    def __init__(self) -> None:
        super().__init__()
        # Register a renderfunc directly so that setting a Style attribute
        # below can be rendered without a KeyError.
        self.renderfuncs = {_DummyRenderType: lambda: "original"}
        self.mystyle = Style(_DummyRenderType(), value="original")


def test_set_renderfunc_updates_renderfuncs_and_styles() -> None:
    reg = _TestRegister()

    # Precondition: only the bootstrap renderfunc is registered.
    assert list(reg.renderfuncs) == [_DummyRenderType]
    assert reg.mystyle == "original"

    original_rule = reg.mystyle.rules[0]

    new_func: Callable = lambda: "rendered"
    reg.set_renderfunc(_DummyRenderType, new_func)

    # Line 150: renderfuncs dict was updated with the new func.
    assert reg.renderfuncs == {_DummyRenderType: new_func}

    # Lines 153-156: the Style attribute was re-set (re-rendered) via setattr.
    assert isinstance(reg.mystyle, Style)
    assert isinstance(reg.mystyle, str)
    assert reg.mystyle == "rendered"
    # The original rule object is preserved through the re-rendering.
    assert reg.mystyle.rules == (original_rule,)

    # Replacing the func for the same rendertype works too (update, not just add).
    another_func: Callable = lambda: "other"
    reg.set_renderfunc(_DummyRenderType, another_func)
    assert reg.renderfuncs == {_DummyRenderType: another_func}
    assert reg.mystyle == "other"
    assert isinstance(reg.mystyle, Style)


def test_set_renderfunc_ignores_non_style_attributes() -> None:
    reg = _TestRegister()
    reg.plain_attr = "not-a-style"  # type: ignore[assignment]

    reg.set_renderfunc(_DummyRenderType, lambda: "changed")

    # Non-Style attributes are untouched by the re-set loop.
    assert reg.plain_attr == "not-a-style"
    assert reg.mystyle == "changed"
    assert isinstance(reg.mystyle, Style)
