# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

import pytest

from sty.primitive import Register


@pytest.fixture
def reg():
    """Provide a fresh Register instance for every test.

    Using a brand-new object per test (instead of the module-level fg/bg/ef/rs
    singletons) guarantees that no global state is polluted and nothing needs
    to be manually restored afterwards.
    """
    return Register()


def test_call_muted_returns_empty_string(reg):
    """Lines 99-100: a muted register must return '' for any call."""
    reg.mute()
    assert reg.is_muted is True

    assert reg(42) == ""          # would otherwise hit eightbit_call
    assert reg("red") == ""       # would otherwise hit getattr
    assert reg(1, 2, 3) == ""     # would otherwise hit rgb_call
    assert reg() == ""            # would otherwise hit the else-branch


def test_call_single_int_dispatches_to_eightbit_call(reg):
    """Lines 104-108: one int argument goes through eightbit_call."""
    received = {}

    def fake_eightbit(x, **kwargs):
        received["args"] = (x,)
        received["kwargs"] = kwargs
        return "EIGHTBIT_RENDERED"

    reg.eightbit_call = fake_eightbit  # plain callable, not a Style -> set as-is

    assert reg(42) == "EIGHTBIT_RENDERED"
    assert received == {"args": (42,), "kwargs": {}}

    # kwargs must be forwarded to the render function as well
    assert reg(7, bold=True) == "EIGHTBIT_RENDERED"
    assert received == {"args": (7,), "kwargs": {"bold": True}}


def test_call_single_str_returns_named_attribute(reg):
    """Lines 113: one string argument is resolved via getattr."""
    reg.red = "RED_STYLE"
    reg.blue = "BLUE_STYLE"

    assert reg("red") == "RED_STYLE"
    assert reg("blue") == "BLUE_STYLE"


def test_call_three_args_dispatches_to_rgb_call(reg):
    """Lines 116-117: three arguments go through rgb_call."""
    received = {}

    def fake_rgb(r, g, b, **kwargs):
        received["args"] = (r, g, b)
        received["kwargs"] = kwargs
        return "RGB_RENDERED"

    reg.rgb_call = fake_rgb  # plain callable, not a Style -> set as-is

    assert reg(10, 20, 30) == "RGB_RENDERED"
    assert received == {"args": (10, 20, 30), "kwargs": {}}

    # kwargs must be forwarded to the render function as well
    assert reg(1, 2, 3, underline=True) == "RGB_RENDERED"
    assert received == {"args": (1, 2, 3), "kwargs": {"underline": True}}


def test_call_wrong_arity_returns_empty_string(reg):
    """Lines 120: any argument count other than 1 or 3 returns ''."""
    assert reg() == ""
    assert reg(1, 2) == ""
    assert reg(1, 2, 3, 4) == ""


def test_call_default_render_functions(reg):
    """Sanity check of the untouched default render callables."""
    # Default eightbit_call is the identity function.
    assert reg(42) == 42
    # Default rgb_call returns the components as a tuple.
    assert reg(1, 2, 3) == (1, 2, 3)
