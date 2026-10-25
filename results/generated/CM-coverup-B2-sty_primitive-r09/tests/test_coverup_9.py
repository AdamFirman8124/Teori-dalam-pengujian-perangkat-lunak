# file: project/sty/primitive.py:202-206
# asked: {"lines": [206], "branches": []}
# gained: {"lines": [206], "branches": []}

import pytest

from sty.primitive import Register, Style


def test_register_copy_returns_deepcopy():
    reg = Register()
    reg.my_style = Style(value="hello")
    reg.payload = ["a", "b"]

    copied = reg.copy()

    # copy() must return a new, distinct Register instance (line 206).
    assert copied is not reg
    assert isinstance(copied, Register)

    # The copied register holds equal, but independent, state.
    assert copied.is_muted == reg.is_muted
    assert copied.renderfuncs == reg.renderfuncs
    assert copied.renderfuncs is not reg.renderfuncs
    assert copied.my_style == reg.my_style
    assert isinstance(copied.my_style, Style)
    assert copied.payload == ["a", "b"]
    assert copied.payload is not reg.payload

    # Mutating the original must not leak into the copy (deepcopy semantics).
    reg.payload.append("c")
    assert copied.payload == ["a", "b"]


def test_register_copy_is_independent_of_renderfuncs():
    reg = Register()
    reg.my_style = Style(value="x")

    copied = reg.copy()

    # Mutating the original's renderfuncs dict must not affect the copy.
    reg.renderfuncs["sentinel"] = lambda x: x
    assert "sentinel" not in copied.renderfuncs
    assert copied.renderfuncs == {}


def test_register_copy_preserves_muted_state():
    reg = Register()
    reg.mute()
    assert reg.is_muted is True

    copied = reg.copy()

    assert copied is not reg
    assert copied.is_muted is True
    assert copied() == ""
