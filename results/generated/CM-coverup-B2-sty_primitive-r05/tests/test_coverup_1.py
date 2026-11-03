# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

"""Tests targeting the previously uncovered lines 99-120 of
sty/primitive.py::Register.__call__.

Every test builds its own fresh ``Register`` instance, so no module-level
sty register (fg/bg/ef/rs) is touched and no state pollution can occur.
"""

import pytest

from sty.primitive import Register


@pytest.fixture
def reg():
    """A fresh Register per test -> complete isolation between tests."""
    return Register()


def test_call_muted_returns_empty_string(reg):
    """Lines 99-100: muted register short-circuits to '' for every arity."""
    reg.mute()
    assert reg.is_muted is True

    assert reg() == ""
    assert reg(42) == ""
    assert reg("red") == ""
    assert reg(1, 2, 3) == ""
    assert reg(1, 2, 3, 4) == ""


def test_call_muted_short_circuits_before_attribute_lookup(reg):
    """Line 99 branch taken even when the str branch would raise."""
    reg.mute()
    # Would raise AttributeError if the muted check were skipped.
    assert reg("no_such_attribute") == ""


def test_call_single_int_dispatches_to_eightbit_call(reg):
    """Lines 107-108: a single int arg is routed to eightbit_call."""
    seen = []

    def fake_eightbit(*args, **kwargs):
        seen.append((args, kwargs))
        return "eightbit-rendered"

    reg.eightbit_call = fake_eightbit  # plain callable -> plain setattr

    assert reg(42) == "eightbit-rendered"
    assert seen == [((42,), {})]


def test_call_single_int_forwards_kwargs_to_eightbit_call(reg):
    """Line 108: **kwargs are forwarded to eightbit_call as well."""
    seen = []

    def fake_eightbit(*args, **kwargs):
        seen.append((args, kwargs))
        return "eightbit-rendered"

    reg.eightbit_call = fake_eightbit

    assert reg(42, bold=True) == "eightbit-rendered"
    assert seen == [((42,), {"bold": True})]


def test_call_single_str_returns_named_attribute(reg):
    """Line 113: a single str arg is looked up as an attribute."""
    reg.red = "red-style"  # plain str bypasses the Style rendering path

    assert reg("red") == "red-style"


def test_call_three_args_dispatches_to_rgb_call(reg):
    """Lines 116-117: three args are routed to rgb_call."""
    seen = []

    def fake_rgb(*args, **kwargs):
        seen.append((args, kwargs))
        return "rgb-rendered"

    reg.rgb_call = fake_rgb

    assert reg(10, 20, 30) == "rgb-rendered"
    assert seen == [((10, 20, 30), {})]


def test_call_three_args_forwards_kwargs_to_rgb_call(reg):
    """Line 117: **kwargs are forwarded to rgb_call as well."""
    seen = []

    def fake_rgb(*args, **kwargs):
        seen.append((args, kwargs))
        return "rgb-rendered"

    reg.rgb_call = fake_rgb

    assert reg(10, 20, 30, bold=True) == "rgb-rendered"
    assert seen == [((10, 20, 30), {"bold": True})]


def test_call_unsupported_arity_returns_empty_string(reg):
    """Line 120: any arity other than 1 or 3 yields ''."""
    assert reg() == ""
    assert reg(1, 2) == ""
    assert reg("a", "b") == ""
    assert reg(1, 2, 3, 4) == ""


def test_call_default_renderers(reg):
    """Sanity check of the default callables used by the dispatch lines."""
    # Default eightbit_call is the identity function.
    assert reg(42) == 42
    # Default rgb_call returns its arguments as a tuple.
    assert reg(1, 2, 3) == (1, 2, 3)


def test_mute_unmute_roundtrip(reg):
    """Lines 99-100 and their recovery via unmute()."""
    reg.red = "red-style"

    reg.mute()
    assert reg("red") == ""
    assert reg(42) == ""

    reg.unmute()
    assert reg.is_muted is False
    assert reg("red") == "red-style"
    assert reg(42) == 42
