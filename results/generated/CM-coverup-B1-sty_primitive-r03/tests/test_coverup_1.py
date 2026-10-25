# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

import pytest

from sty.primitive import Register


@pytest.fixture
def reg():
    """A fresh Register instance per test, so no global state (e.g. sty.fg) is touched."""
    return Register()


def test_call_muted_returns_empty_string(reg):
    reg.mute()
    assert reg.is_muted is True
    # All call shapes short-circuit to "" when muted.
    assert reg(42) == ""
    assert reg("red") == ""
    assert reg(1, 2, 3) == ""
    assert reg() == ""

    # Cleanup: restore the instance so post-mute behavior is verified.
    reg.unmute()
    assert reg.is_muted is False
    assert reg(42) == 42  # default eightbit_call is identity


def test_call_single_int_arg_uses_eightbit_call(reg):
    calls = []

    def fake_eightbit(x, **kwargs):
        calls.append((x, kwargs))
        return "eight"

    object.__setattr__(reg, "eightbit_call", fake_eightbit)

    result = reg(7, bold=True)

    assert result == "eight"
    assert calls == [(7, {"bold": True})]  # args and kwargs forwarded


def test_call_single_str_arg_returns_matching_attribute(reg):
    # Bypass Register.__setattr__ (which only accepts Style/callables)
    # to install a plain string attribute.
    object.__setattr__(reg, "myattr", "rendered")

    result = reg("myattr")

    assert result == "rendered"


def test_call_three_args_uses_rgb_call(reg):
    calls = []

    def fake_rgb(r, g, b, **kwargs):
        calls.append((r, g, b, kwargs))
        return "rgb"

    object.__setattr__(reg, "rgb_call", fake_rgb)

    result = reg(10, 20, 30, underline=True)

    assert result == "rgb"
    assert calls == [(10, 20, 30, {"underline": True})]  # args and kwargs forwarded


@pytest.mark.parametrize("args", [(), (1, 2), (1, 2, 3, 4), (1, 2, 3, 4, 5)])
def test_call_other_arity_returns_empty_string(reg, args):
    assert reg(*args) == ""
