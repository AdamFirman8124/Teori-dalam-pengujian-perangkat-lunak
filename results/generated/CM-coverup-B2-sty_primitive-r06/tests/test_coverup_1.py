# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

import pytest

from sty.primitive import Register


@pytest.fixture
def reg():
    """A fresh Register instance for every test, so no state leaks between tests."""
    return Register()


def test_call_returns_empty_str_when_muted(reg, monkeypatch):
    """Lines 99-100: a muted register short-circuits to '' for every call shape."""
    reg.mute()
    assert reg.is_muted is True

    # Record any dispatch attempts; none must happen while muted.
    calls = []
    monkeypatch.setattr(reg, "eightbit_call", lambda *a, **kw: calls.append(("8bit", a, kw)) or "x")
    monkeypatch.setattr(reg, "rgb_call", lambda *a, **kw: calls.append(("rgb", a, kw)) or "x")

    assert reg(42) == ""          # 1 int arg
    assert reg("red") == ""       # 1 str arg
    assert reg(1, 2, 3) == ""     # 3 args
    assert reg() == ""            # 0 args
    assert calls == []            # render functions were never invoked


def test_call_single_int_uses_eightbit_call(reg, monkeypatch):
    """Lines 104, 107-108: one int arg is forwarded to eightbit_call."""
    calls = []

    def fake_eightbit(*args, **kwargs):
        calls.append((args, kwargs))
        return "eightbit-rendered"

    monkeypatch.setattr(reg, "eightbit_call", fake_eightbit)

    assert reg(42) == "eightbit-rendered"
    assert calls == [((42,), {})]


def test_call_single_int_forwards_kwargs_to_eightbit_call(reg, monkeypatch):
    """Line 108: kwargs are forwarded along with the int arg."""
    calls = []

    def fake_eightbit(*args, **kwargs):
        calls.append((args, kwargs))
        return "eightbit-rendered"

    monkeypatch.setattr(reg, "eightbit_call", fake_eightbit)

    assert reg(7, bold=True) == "eightbit-rendered"
    assert calls == [((7,), {"bold": True})]


def test_call_single_str_returns_named_attribute(reg):
    """Line 113: one str arg returns the attribute with the matching name.

    A plain str is not a Style, so Register.__setattr__ stores it as a
    normal instance attribute, which getattr() then retrieves.
    """
    reg.red = "RED"
    assert reg("red") == "RED"


def test_call_single_str_unknown_name_raises(reg):
    """Line 113: getattr on an unknown name propagates AttributeError."""
    with pytest.raises(AttributeError):
        reg("no_such_attribute")


def test_call_three_args_uses_rgb_call(reg, monkeypatch):
    """Lines 116-117: three args are forwarded to rgb_call."""
    calls = []

    def fake_rgb(*args, **kwargs):
        calls.append((args, kwargs))
        return "rgb-rendered"

    monkeypatch.setattr(reg, "rgb_call", fake_rgb)

    assert reg(102, 49, 42) == "rgb-rendered"
    assert calls == [((102, 49, 42), {})]


def test_call_other_arities_return_empty_str(reg, monkeypatch):
    """Line 120: any arity other than 1 or 3 yields '' without dispatching."""
    calls = []
    monkeypatch.setattr(reg, "eightbit_call", lambda *a, **kw: calls.append(("8bit", a, kw)) or "x")
    monkeypatch.setattr(reg, "rgb_call", lambda *a, **kw: calls.append(("rgb", a, kw)) or "x")

    assert reg() == ""            # 0 args
    assert reg(1, 2) == ""        # 2 args
    assert reg(1, 2, 3, 4) == ""  # 4 args
    assert calls == []            # no render function was invoked
