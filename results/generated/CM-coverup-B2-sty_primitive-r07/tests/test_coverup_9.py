# file: project/sty/primitive.py:202-206
# asked: {"lines": [206], "branches": []}
# gained: {"lines": [206], "branches": []}

from sty.primitive import Register


def test_copy_returns_independent_deepcopy():
    reg = Register()
    reg.renderfuncs["fg"] = lambda s: s
    reg.renderfuncs["nested"] = {"values": [1, 2, 3]}

    clone = reg.copy()

    assert isinstance(clone, Register)
    assert clone is not reg
    assert clone.renderfuncs == reg.renderfuncs
    assert clone.renderfuncs is not reg.renderfuncs
    assert clone.renderfuncs["nested"] is not reg.renderfuncs["nested"]
    assert clone.renderfuncs["nested"]["values"] is not reg.renderfuncs["nested"]["values"]

    # mutating the copy must not leak into the original
    clone.renderfuncs["bg"] = lambda s: s
    clone.renderfuncs["nested"]["values"].append(4)
    assert "bg" not in reg.renderfuncs
    assert reg.renderfuncs["nested"]["values"] == [1, 2, 3]


def test_copy_preserves_mute_state_without_sharing_it():
    reg = Register()
    reg.mute()

    clone = reg.copy()

    assert clone.is_muted is True
    assert clone.is_muted == reg.is_muted

    clone.unmute()
    assert clone.is_muted is False
    assert reg.is_muted is True


def test_copy_of_fresh_register_keeps_default_callables():
    reg = Register()

    clone = reg.copy()

    assert clone.eightbit_call is reg.eightbit_call
    assert clone.rgb_call is reg.rgb_call
    assert clone.eightbit_call(7) == 7
    assert clone.rgb_call(1, 2, 3) == (1, 2, 3)
    assert clone.is_muted is False
