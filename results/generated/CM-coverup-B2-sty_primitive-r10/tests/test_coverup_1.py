# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

import pytest

from sty.primitive import Register


class TestRegisterCallCoverage:
    """Covers Register.__call__ lines 99-120: muted early-return, 8bit call,
    named-attribute lookup, 24bit rgb call, and fallback empty string."""

    def test_call_returns_empty_str_when_muted(self):
        reg = Register()
        reg.mute()
        assert reg.is_muted is True
        # All branches (1 int arg, 1 str arg, 3 args, other) short-circuit.
        assert reg(42) == ""
        assert reg("red") == ""
        assert reg(1, 2, 3) == ""
        assert reg() == ""
        # Cleanup: restore state on this isolated instance.
        reg.unmute()
        assert reg.is_muted is False

    def test_call_single_int_uses_eightbit_call(self):
        reg = Register()
        # Default eightbit_call is identity, but use a sentinel to prove
        # the eightbit branch (line 108) is the one executed.
        reg.eightbit_call = lambda x: f"eightbit:{x}"
        result = reg(42)
        assert result == "eightbit:42"

    def test_call_single_str_returns_matching_attribute(self):
        reg = Register()
        # A plain (non-Style) string attribute bypasses rendering and is
        # returned verbatim by the getattr branch (line 113).
        reg.mycolor = "rendered-mycolor"
        assert reg("mycolor") == "rendered-mycolor"

    def test_call_three_args_uses_rgb_call(self):
        reg = Register()
        # Default rgb_call returns the tuple; use a sentinel to prove the
        # rgb branch (line 117) is the one executed.
        reg.rgb_call = lambda r, g, b: f"rgb:{r}-{g}-{b}"
        result = reg(10, 20, 30)
        assert result == "rgb:10-20-30"

    @pytest.mark.parametrize("args", [(), (1, 2), (1, 2, 3, 4)])
    def test_call_other_arity_returns_empty_str(self, args):
        reg = Register()
        assert reg(*args) == ""

    def test_call_unmuted_after_mute_restores_behavior(self):
        reg = Register()
        reg.mute()
        assert reg(42) == ""
        reg.unmute()
        # Default eightbit_call is the identity function.
        assert reg(42) == 42
        assert reg(1, 2, 3) == (1, 2, 3)
