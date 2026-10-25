# file: project/sty/primitive.py:202-206
# asked: {"lines": [206], "branches": []}
# gained: {"lines": [206], "branches": []}

from sty.primitive import Register


def test_copy_returns_new_register_instance():
    reg = Register()
    copied = reg.copy()
    try:
        assert isinstance(copied, Register)
        assert copied is not reg
        assert copied.__dict__ == reg.__dict__
        assert copied.renderfuncs is not reg.renderfuncs
    finally:
        del reg
        del copied


def test_copy_is_deepcopy_and_independent():
    reg = Register()
    try:
        reg.renderfuncs["custom"] = {"nested": [1, 2, 3]}
        copied = reg.copy()
        try:
            # postconditions: equal value but distinct objects (deep)
            assert copied.renderfuncs == reg.renderfuncs
            assert copied.renderfuncs is not reg.renderfuncs
            assert copied.renderfuncs["custom"] is not reg.renderfuncs["custom"]
            assert copied.renderfuncs["custom"]["nested"] is not reg.renderfuncs["custom"]["nested"]

            # mutating original does not affect copy
            reg.renderfuncs["custom"]["nested"].append(4)
            assert copied.renderfuncs["custom"]["nested"] == [1, 2, 3]

            # mutating copy does not affect original
            copied.renderfuncs["other"] = "x"
            assert "other" not in reg.renderfuncs
        finally:
            del copied
    finally:
        del reg


def test_copy_preserves_muted_state_and_independence():
    reg = Register()
    try:
        reg.mute()
        assert reg.is_muted is True
        copied = reg.copy()
        try:
            assert copied.is_muted is True
            # independence of mute flag
            copied.unmute()
            assert copied.is_muted is False
            assert reg.is_muted is True
        finally:
            del copied

        reg.unmute()
        copied2 = reg.copy()
        try:
            assert copied2.is_muted is False
        finally:
            del copied2
    finally:
        del reg
