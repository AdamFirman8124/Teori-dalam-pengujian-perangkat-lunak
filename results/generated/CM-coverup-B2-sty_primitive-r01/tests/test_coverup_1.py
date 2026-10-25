# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

import pytest

from sty.primitive import Register


def test_register_call_returns_empty_string_when_muted(monkeypatch):
    register = Register()
    calls = []

    monkeypatch.setattr(
        register,
        "eightbit_call",
        lambda *args, **kwargs: calls.append(("eightbit", args, kwargs)),
    )
    monkeypatch.setattr(
        register,
        "rgb_call",
        lambda *args, **kwargs: calls.append(("rgb", args, kwargs)),
    )
    register.mute()

    assert register(42) == ""
    assert register(1, 2, 3) == ""
    assert register.is_muted is True
    assert calls == []


def test_register_call_with_single_integer_uses_eightbit_call(monkeypatch):
    register = Register()
    received = {}

    def fake_eightbit_call(value, **kwargs):
        received["value"] = value
        received["kwargs"] = kwargs
        return "eightbit-result"

    monkeypatch.setattr(register, "eightbit_call", fake_eightbit_call)

    result = register(42, option="value")

    assert result == "eightbit-result"
    assert received == {"value": 42, "kwargs": {"option": "value"}}


def test_register_call_with_single_string_returns_named_attribute():
    register = Register()
    register.red = "red-style"

    assert register("red") == "red-style"


def test_register_call_with_three_arguments_uses_rgb_call(monkeypatch):
    register = Register()
    received = {}

    def fake_rgb_call(red, green, blue, **kwargs):
        received["components"] = (red, green, blue)
        received["kwargs"] = kwargs
        return "rgb-result"

    monkeypatch.setattr(register, "rgb_call", fake_rgb_call)

    result = register(102, 49, 42, option="value")

    assert result == "rgb-result"
    assert received == {
        "components": (102, 49, 42),
        "kwargs": {"option": "value"},
    }


@pytest.mark.parametrize("args", [(), (1, 2), (1, 2, 3, 4)])
def test_register_call_with_unsupported_argument_count_returns_empty_string(args):
    register = Register()

    assert register(*args) == ""
