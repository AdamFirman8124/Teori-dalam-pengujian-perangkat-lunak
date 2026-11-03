# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

"""
Coverage tests for sty.primitive.Register.__call__ (lines 99-120).

Every test constructs its own private Register instance, so no module-level
state (such as the global fg/bg/ef/rs registers) is read, mutated or leaked:
each instance is simply garbage-collected when its test finishes.
"""

import pytest

from sty.primitive import Register


@pytest.fixture
def reg():
    """Provide a pristine Register instance, isolated from global state."""
    return Register()


def test_call_muted_short_circuits_to_empty_string(reg):
    reg.mute()
    assert reg.is_muted is True

    # While muted, every call path must short-circuit to "" (lines 99-100),
    # before any dispatch logic runs.
    assert reg() == ""
    assert reg(42) == ""
    assert reg("red") == ""
    assert reg(1, 2, 3) == ""
    assert reg(1, 2, 3, 4) == ""


def test_register_is_unmuted_by_default(reg):
    # Baseline for the muted branch: the flag starts out False.
    assert reg.is_muted is False


def test_call_single_int_arg_dispatches_to_eightbit_call(reg):
    # Replace the default identity renderer so we can observe the dispatch.
    reg.eightbit_call = lambda x, **kwargs: f"eightbit:{x}"

    assert reg(42) == "eightbit:42"
    # Keyword arguments must be forwarded to eightbit_call as well.
    assert reg(7, bold=True) == "eightbit:7"


def test_call_single_str_arg_returns_matching_attribute(reg):
    # Plain strings are stored verbatim by Register.__setattr__.
    reg.red = "RED"
    reg.blue = "BLUE"

    assert reg("red") == "RED"
    assert reg("blue") == "BLUE"


def test_call_single_unknown_str_raises_attribute_error(reg):
    # Line 113 resolves the name via getattr; unknown names must raise.
    with pytest.raises(AttributeError):
        reg("no_such_color")


def test_call_three_args_dispatch_to_rgb_call(reg):
    # Replace the default renderer so we can observe the dispatch.
    reg.rgb_call = lambda r, g, b, **kwargs: f"rgb:{r}-{g}-{b}"

    assert reg(10, 20, 30) == "rgb:10-20-30"
    # Keyword arguments must be forwarded to rgb_call as well.
    assert reg(1, 2, 3, bold=True) == "rgb:1-2-3"


@pytest.mark.parametrize(
    "args",
    [
        (),                # zero args
        (1, 2),            # two args
        (1, 2, 3, 4),      # four args
        ("a", "b", "c", "d"),
    ],
)
def test_call_unsupported_arity_returns_empty_string(reg, args):
    # Any arity other than 1 or 3 falls through to the final ``return ""``.
    # (Exactly three args is a *supported* arity: it dispatches to rgb_call.)
    assert reg(*args) == ""
