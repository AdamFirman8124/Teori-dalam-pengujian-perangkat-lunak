# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

import pytest

from sty.primitive import Register


@pytest.fixture
def reg():
    """A fresh Register instance per test to avoid any state pollution."""
    return Register()


def test_call_returns_empty_str_when_muted(reg):
    reg.mute()
    assert reg.is_muted is True

    # All branches short-circuit to "" when muted.
    assert reg(42) == ""
    assert reg("red") == ""
    assert reg(1, 2, 3) == ""
    assert reg() == ""


def test_call_single_int_arg_uses_eightbit_call(reg):
    reg.eightbit_call = lambda x, **kwargs: f"eightbit:{x}:{kwargs.get('bold', False)}"
    result = reg(42, bold=True)
    assert result == "eightbit:42:True"


def test_call_single_str_arg_returns_matching_attribute(reg):
    # Plain strings bypass the Style rendering in __setattr__.
    reg.red = "RED_RENDERED"
    reg.blue = "BLUE_RENDERED"

    assert reg("red") == "RED_RENDERED"
    assert reg("blue") == "BLUE_RENDERED"


def test_call_three_args_uses_rgb_call(reg):
    reg.rgb_call = lambda r, g, b: f"rgb:{r},{g},{b}"
    result = reg(10, 20, 30)
    assert result == "rgb:10,20,30"


def test_call_other_arity_returns_empty_str(reg):
    # Zero args and more than 3 args fall into the final else branch.
    assert reg() == ""
    assert reg(1, 2, 3, 4) == ""
    assert reg("a", "b") == ""
