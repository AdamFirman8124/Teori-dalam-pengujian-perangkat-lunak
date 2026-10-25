# file: project/sty/primitive.py:202-206
# asked: {"lines": [206], "branches": []}
# gained: {"lines": [206], "branches": []}

from copy import deepcopy

import pytest

from sty.primitive import Register


def _make_register():
    reg = Register()
    reg.renderfuncs["fg"] = lambda x: f"fg-{x}"
    reg.renderfuncs["bg"] = lambda x: f"bg-{x}"
    return reg


def test_copy_returns_deepcopy_of_register():
    reg = _make_register()

    clone = reg.copy()

    # postconditions: a real copy, not the same object
    assert isinstance(clone, Register)
    assert clone is not reg
    assert clone.renderfuncs == reg.renderfuncs
    assert clone.renderfuncs is not reg.renderfuncs
    assert clone.is_muted == reg.is_muted
    assert clone.eightbit_call is reg.eightbit_call
    assert clone.rgb_call is reg.rgb_call

    # mutating the copy must not leak into the original
    clone.renderfuncs["ef"] = lambda x: f"ef-{x}"
    assert "ef" not in reg.renderfuncs
    del clone.renderfuncs["fg"]
    assert "fg" in reg.renderfuncs

    # and the copy behaves like the original
    assert clone(1) == reg(1)


def test_copy_preserves_muted_state():
    reg = _make_register()
    reg.mute()

    clone = reg.copy()

    assert clone.is_muted is True
    assert reg.is_muted is True
    assert clone is not reg

    clone.unmute()
    assert clone.is_muted is False
    assert reg.is_muted is True


def test_copy_matches_stdlib_deepcopy():
    reg = _make_register()
    reg.mute()

    clone = reg.copy()
    reference = deepcopy(reg)

    assert clone.renderfuncs == reference.renderfuncs
    assert clone.is_muted == reference.is_muted
    assert clone.eightbit_call is reference.eightbit_call
    assert clone.rgb_call is reference.rgb_call
