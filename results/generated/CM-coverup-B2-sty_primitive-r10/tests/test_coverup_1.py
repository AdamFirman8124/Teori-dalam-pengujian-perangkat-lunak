# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

"""Tests for sty/primitive.py::Register.__call__ (previously uncovered lines 99-120).

Every test operates on a freshly created ``Register`` instance, so the
module-level singletons (fg, bg, ef, rs) are never touched and no state can
leak between tests.  Where an instance attribute is temporarily replaced,
pytest's ``monkeypatch`` fixture restores the original value automatically.
"""

import pytest

from sty.primitive import Register


@pytest.fixture
def reg():
    """A brand-new, isolated Register instance for each test."""
    return Register()


class TestRegisterCallMuted:
    def test_muted_register_returns_empty_string_for_every_arity(self, reg):
        """Lines 99-100: a muted register returns '' no matter how it is called."""
        reg.eightbit_call = lambda x: f"8bit({x})"
        reg.rgb_call = lambda r, g, b: f"rgb({r},{g},{b})"

        reg.mute()
        assert reg.is_muted is True

        assert reg() == ""
        assert reg(42) == ""
        assert reg("mycolor") == ""
        assert reg(1, 2, 3) == ""
        assert reg(1, 2, 3, 4) == ""

        # Postcondition: unmuting restores normal dispatch, proving the empty
        # strings above really came from the muted branch (lines 99-100).
        reg.unmute()
        assert reg.is_muted is False
        assert reg(42) == "8bit(42)"
        assert reg(1, 2, 3) == "rgb(1,2,3)"


class TestRegisterCallSingleArgument:
    def test_single_int_arg_is_dispatched_to_eightbit_call(self, reg, monkeypatch):
        """Lines 104, 107-108: one int argument is routed to eightbit_call."""
        calls = []

        def spy_eightbit_call(*args, **kwargs):
            calls.append((args, kwargs))
            return "EIGHTBIT-RENDERED"

        monkeypatch.setattr(reg, "eightbit_call", spy_eightbit_call)

        assert reg(42) == "EIGHTBIT-RENDERED"
        assert calls == [((42,), {})]

        # Keyword arguments must be forwarded to the renderer as well.
        assert reg(7, bold=True) == "EIGHTBIT-RENDERED"
        assert calls[-1] == ((7,), {"bold": True})

    def test_single_int_arg_uses_default_identity_renderer(self, reg):
        """Line 108: with the default renderer the int is returned unchanged,
        which proves the call was routed through eightbit_call."""
        assert reg(42) == 42

    def test_single_str_arg_returns_attribute_with_that_name(self, reg):
        """Line 113: one str argument is looked up as an attribute on the register."""
        reg.mycolor = "MYCOLOR-ESCAPE-SEQ"
        assert reg("mycolor") == "MYCOLOR-ESCAPE-SEQ"

    def test_single_str_arg_with_unknown_name_raises(self, reg):
        """Line 113: getattr on an unknown name raises AttributeError."""
        with pytest.raises(AttributeError):
            reg("does_not_exist")


class TestRegisterCallThreeArguments:
    def test_three_args_are_dispatched_to_rgb_call(self, reg, monkeypatch):
        """Lines 116-117: three arguments are routed to rgb_call."""
        calls = []

        def spy_rgb_call(*args, **kwargs):
            calls.append((args, kwargs))
            return "RGB-RENDERED"

        monkeypatch.setattr(reg, "rgb_call", spy_rgb_call)

        assert reg(1, 2, 3) == "RGB-RENDERED"
        assert calls == [((1, 2, 3), {})]

        # Keyword arguments must be forwarded to the renderer as well.
        assert reg(10, 20, 30, underline=True) == "RGB-RENDERED"
        assert calls[-1] == ((10, 20, 30), {"underline": True})

    def test_three_args_use_default_rgb_renderer(self, reg):
        """Line 117: with the default renderer the tuple is returned unchanged,
        which proves the call was routed through rgb_call."""
        assert reg(1, 2, 3) == (1, 2, 3)


class TestRegisterCallOtherArities:
    @pytest.mark.parametrize("args", [(), (1, 2), ("a", "b"), (1, 2, 3, 4)])
    def test_unsupported_arity_returns_empty_string(self, reg, args):
        """Line 120: zero, two or four arguments yield ''."""
        assert reg(*args) == ""
