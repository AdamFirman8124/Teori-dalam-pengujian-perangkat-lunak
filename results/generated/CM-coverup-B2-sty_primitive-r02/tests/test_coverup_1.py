# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

import pytest

from sty.primitive import Register


@pytest.fixture
def reg():
    """Provide a fresh Register instance per test so no shared/global state is touched."""
    r = Register()
    # A plain (non-Style) attribute: Register.__setattr__ stores it verbatim,
    # which is enough to exercise the string-lookup branch of __call__.
    r.red = "RED"
    yield r
    # Defensive cleanup: the object is per-test anyway, so nothing leaks.
    r.unmute()


def test_call_muted_returns_empty_string(reg):
    reg.mute()
    assert reg.is_muted is True

    # All call forms short-circuit to "" while muted.
    assert reg(42) == ""
    assert reg("red") == ""
    assert reg(10, 20, 30) == ""
    assert reg() == ""

    # The early return must not invoke the render functions.
    calls = []

    def spy(x):
        calls.append(x)
        return x

    reg.eightbit_call = spy
    assert reg(1) == ""
    assert calls == []

    # Attributes keep their values while muted (mute does not delete them).
    assert reg.red == "RED"


def test_call_unmute_restores_behaviour(reg):
    reg.mute()
    assert reg(42) == ""
    reg.unmute()
    assert reg.is_muted is False

    assert reg(42) == 42
    assert reg("red") == "RED"
    assert reg(1, 2, 3) == (1, 2, 3)


def test_call_single_int_uses_eightbit_call(reg):
    # Default eightbit_call is the identity function.
    assert reg(42) == 42

    # kwargs are forwarded to the eightbit renderer.
    reg.eightbit_call = lambda x, **kwargs: (x, kwargs)
    assert reg(7, foo="bar") == (7, {"foo": "bar"})


def test_call_single_str_returns_named_attribute(reg):
    assert reg("red") == "RED"
    # Unknown names still hit getattr (and raise AttributeError as expected).
    with pytest.raises(AttributeError):
        reg("does_not_exist")


def test_call_three_args_uses_rgb_call(reg):
    # Default rgb_call simply returns the tuple of the three components.
    assert reg(10, 20, 30) == (10, 20, 30)

    # kwargs are forwarded to the rgb renderer.
    reg.rgb_call = lambda r, g, b, **kwargs: (r, g, b, kwargs)
    assert reg(1, 2, 3, key="val") == (1, 2, 3, {"key": "val"})


def test_call_wrong_arity_returns_empty_string(reg):
    # Arities other than 1 and 3 fall through to the final `return ""`.
    assert reg() == ""
    assert reg(1, 2) == ""
    assert reg(1, 2, 3, 4) == ""
    assert reg("a", "b") == ""
