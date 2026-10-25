# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

from unittest.mock import Mock

from sty.primitive import Register


def test_register_call_returns_empty_string_when_muted(monkeypatch):
    register = Register()
    eightbit_call = Mock()
    rgb_call = Mock()

    monkeypatch.setattr(register, "eightbit_call", eightbit_call)
    monkeypatch.setattr(register, "rgb_call", rgb_call)
    monkeypatch.setattr(register, "is_muted", True)

    assert register(42) == ""
    assert register(1, 2, 3) == ""
    eightbit_call.assert_not_called()
    rgb_call.assert_not_called()


def test_register_call_with_one_integer_uses_eightbit_call(monkeypatch):
    register = Register()
    eightbit_call = Mock(return_value="eight-bit result")
    monkeypatch.setattr(register, "eightbit_call", eightbit_call)

    result = register(42, option="value")

    assert result == "eight-bit result"
    eightbit_call.assert_called_once_with(42, option="value")


def test_register_call_with_one_string_returns_named_attribute(monkeypatch):
    register = Register()
    expected = object()
    monkeypatch.setattr(register, "red", expected, raising=False)

    assert register("red") is expected


def test_register_call_with_three_arguments_uses_rgb_call(monkeypatch):
    register = Register()
    rgb_call = Mock(return_value="rgb result")
    monkeypatch.setattr(register, "rgb_call", rgb_call)

    result = register(102, 49, 42, option="value")

    assert result == "rgb result"
    rgb_call.assert_called_once_with(102, 49, 42, option="value")


def test_register_call_with_unsupported_argument_counts_returns_empty_string():
    register = Register()

    assert register() == ""
    assert register(1, 2) == ""
    assert register(1, 2, 3, 4) == ""
