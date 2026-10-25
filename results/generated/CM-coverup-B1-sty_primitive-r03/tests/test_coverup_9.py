# file: project/sty/primitive.py:202-206
# asked: {"lines": [206], "branches": []}
# gained: {"lines": [206], "branches": []}

import pytest

from sty.primitive import Register, Style


def test_register_copy_deepcopies_attributes():
    reg = Register()
    # Register.__setattr__ re-renders Style values, so capture the stored
    # (rendered) style rather than the raw object we assigned.
    reg.my_style = Style(value="hello")
    original_style = reg.my_style

    copied = reg.copy()

    # copy() must return a new, distinct Register instance (line 206).
    assert copied is not reg
    assert isinstance(copied, Register)

    # The copied register holds equal, but independent, state.
    assert copied.is_muted == reg.is_muted
    assert copied.renderfuncs == reg.renderfuncs
    assert copied.my_style == original_style
    assert copied.my_style is not original_style

    # Mutating the original must not leak into the copy (deepcopy semantics).
    reg.my_style = Style(value="changed")
    assert copied.my_style == original_style


def test_register_copy_is_independent_of_renderfuncs():
    reg = Register()
    reg.my_style = Style(value="x")

    copied = reg.copy()

    # Mutating the original's renderfuncs dict must not affect the copy.
    reg.renderfuncs["sentinel"] = lambda x: x
    assert "sentinel" not in copied.renderfuncs
