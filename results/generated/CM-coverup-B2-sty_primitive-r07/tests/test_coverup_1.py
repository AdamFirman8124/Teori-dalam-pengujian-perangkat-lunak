# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

"""Tests for Register.__call__ in sty/primitive.py (previously uncovered lines 99-120).

These tests only ever instantiate fresh Register objects; the module-level
registers (fg, bg, ef, rs) are never touched, so no global state can be
polluted and no cleanup/monkeypatching is required.
"""

import pytest

from sty.primitive import Register


@pytest.fixture
def reg():
    """A fresh Register instance for each test."""
    return Register()


class TestRegisterCall:
    def test_call_returns_empty_string_when_muted(self, reg):
        """Lines 99-100: a muted register short-circuits to '' for every call shape."""
        reg.mute()
        assert reg.is_muted is True

        assert reg(42) == ""          # single int
        assert reg("red") == ""       # single str (must not raise AttributeError)
        assert reg(1, 2, 3) == ""     # three args
        assert reg() == ""            # zero args

    def test_call_after_unmute_dispatches_normally(self, reg):
        """After mute()/unmute(), the is_muted branch is False again."""
        reg.mute()
        reg.unmute()
        assert reg.is_muted is False
        # Default eightbit_call is the identity function.
        assert reg(42) == 42

    def test_call_single_int_arg_uses_eightbit_call(self, reg):
        """Lines 104, 107-108: one int arg is routed to eightbit_call (with kwargs)."""
        reg.eightbit_call = lambda x, **kwargs: f"eightbit:{x}:{kwargs.get('flag')}"
        result = reg(42, flag="kw")
        assert result == "eightbit:42:kw"

    def test_call_single_str_arg_returns_matching_attribute(self, reg):
        """Line 113: one str arg returns the attribute with that name.

        A plain str is assigned, which bypasses the Style rendering logic in
        Register.__setattr__ (isinstance check fails, value stored as-is).
        """
        reg.red = "RED"
        assert reg("red") == "RED"

    def test_call_single_unknown_str_arg_raises_attribute_error(self, reg):
        """Line 113: getattr semantics are preserved for unknown names."""
        with pytest.raises(AttributeError):
            reg("no_such_attribute")

    def test_call_three_args_uses_rgb_call(self, reg):
        """Lines 116-117: three args are routed to rgb_call (with kwargs)."""
        reg.rgb_call = lambda r, g, b, **kwargs: f"rgb:{r}-{g}-{b}:{kwargs.get('flag')}"
        result = reg(10, 20, 30, flag="kw")
        assert result == "rgb:10-20-30:kw"

    def test_call_default_renderers(self, reg):
        """Sanity check of the default renderers set in __init__."""
        assert reg(7) == 7            # eightbit_call defaults to identity
        assert reg(1, 2, 3) == (1, 2, 3)  # rgb_call defaults to tuple builder

    def test_call_with_other_arities_returns_empty_string(self, reg):
        """Line 120: any arity other than 1 or 3 yields ''."""
        assert reg() == ""
        assert reg(1, 2) == ""
        assert reg(1, 2, 3, 4) == ""
