# file: project/sty/primitive.py:142-156
# asked: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}
# gained: {"lines": [150, 153, 154, 155, 156], "branches": [[153, 0], [153, 154], [155, 153], [155, 156]]}

from typing import Callable

import pytest

from sty import Register, Style
from sty.rendertype import RenderType


class _DummyRenderType(RenderType):
    """Minimal concrete RenderType used only for testing."""


def _identity_func(x: str) -> str:
    return x


class _TestRegister(Register):
    """Register subclass with one Style attribute, isolated from global registers."""

    def __init__(self) -> None:
        super().__init__()
        # A Style without RenderType rules can be set before any renderfunc is
        # registered (Register.__setattr__ renders rules via _render_rules,
        # which would raise KeyError for unregistered rule types).
        self.mystyle = Style(value="original")


def test_set_renderfunc_updates_renderfuncs_and_styles() -> None:
    reg = _TestRegister()

    # Precondition: no renderfuncs registered yet.
    assert reg.renderfuncs == {}

    new_func: Callable = lambda x: f"rendered({x})"
    reg.set_renderfunc(_DummyRenderType, new_func)

    # Line 150: renderfuncs dict was updated with the new func.
    assert reg.renderfuncs == {_DummyRenderType: new_func}

    # Lines 153-156: the Style attribute was re-set (re-rendered) via setattr.
    # Register.__setattr__ re-renders Style instances, so the attribute must
    # still be a Style instance afterwards.
    assert isinstance(reg.mystyle, Style)
    assert isinstance(reg.mystyle, str)

    # Replacing the func for the same rendertype works too (update, not just add).
    another_func: Callable = lambda x: f"other({x})"
    reg.set_renderfunc(_DummyRenderType, another_func)
    assert reg.renderfuncs == {_DummyRenderType: another_func}
    assert isinstance(reg.mystyle, Style)


def test_set_renderfunc_ignores_non_style_attributes() -> None:
    reg = _TestRegister()
    reg.plain_attr = "not-a-style"  # type: ignore[assignment]

    reg.set_renderfunc(_DummyRenderType, _identity_func)

    # Non-Style attributes are untouched by the re-set loop.
    assert reg.plain_attr == "not-a-style"
    assert reg.renderfuncs == {_DummyRenderType: _identity_func}
    assert isinstance(reg.mystyle, Style)
