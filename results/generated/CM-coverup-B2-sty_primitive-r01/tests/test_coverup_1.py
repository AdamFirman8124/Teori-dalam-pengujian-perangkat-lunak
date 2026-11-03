# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

"""Tests for sty.primitive.Register.__call__ (previously uncovered lines 99-120).

Every test operates on a fresh, function-scoped Register instance, so no
module-level register (fg/bg/ef/rs) and no class attribute is ever mutated.
The only cross-test mutation (is_muted) is done through monkeypatch, which
restores the original value automatically.
"""

import pytest

from sty.primitive import Register


@pytest.fixture()
def reg():
    """A fresh Register with recording stub renderers and one named attribute.

    Plain values (lists, functions, strings) are stored verbatim by
    Register.__setattr__ because they are not Style instances.
    """
    r = Register()
    r.calls = []

    def eightbit_call(value, **kwargs):
        r.calls.append(("eightbit", value, kwargs))
        return "eightbit({})".format(value)

    def rgb_call(red, green, blue, **kwargs):
        r.calls.append(("rgb", red, green, blue, kwargs))
        return "rgb({},{},{})".format(red, green, blue)

    r.eightbit_call = eightbit_call
    r.rgb_call = rgb_call
    r.red = "RED"
    return r


def test_call_single_int_delegates_to_eightbit_call(reg):
    assert reg(42) == "eightbit(42)"
    assert reg.calls == [("eightbit", 42, {})]


def test_call_single_int_forwards_kwargs_to_eightbit_call(reg):
    assert reg(42, bold=True) == "eightbit(42)"
    assert reg.calls == [("eightbit", 42, {"bold": True})]


def test_call_single_str_returns_matching_attribute(reg):
    assert reg("red") == "RED"
    assert reg.calls == []  # no render function may be invoked on this path


def test_call_single_str_unknown_name_raises_attribute_error(reg):
    with pytest.raises(AttributeError):
        reg("does_not_exist")


def test_call_three_args_delegates_to_rgb_call(reg):
    assert reg(10, 20, 30) == "rgb(10,20,30)"
    assert reg.calls == [("rgb", 10, 20, 30, {})]


def test_call_three_args_forwards_kwargs_to_rgb_call(reg):
    assert reg(10, 20, 30, underline=True) == "rgb(10,20,30)"
    assert reg.calls == [("rgb", 10, 20, 30, {"underline": True})]


@pytest.mark.parametrize("args", [(), (1, 2), (1, 2, 3, 4)])
def test_call_with_other_arities_returns_empty_string(reg, args):
    assert reg(*args) == ""
    assert reg.calls == []


def test_call_returns_empty_string_for_every_arity_when_muted(reg, monkeypatch):
    monkeypatch.setattr(reg, "is_muted", True)  # restored automatically

    assert reg(42) == ""
    assert reg("red") == ""
    assert reg(1, 2, 3) == ""
    assert reg() == ""
    assert reg.calls == []  # a muted register must not render anything
