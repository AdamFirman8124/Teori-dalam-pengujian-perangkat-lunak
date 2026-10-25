# file: project/sty/primitive.py:93-120
# asked: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}
# gained: {"lines": [99, 100, 102, 104, 107, 108, 113, 116, 117, 120], "branches": [[99, 100], [99, 102], [104, 107], [104, 116], [107, 108], [107, 113], [116, 117], [116, 120]]}

from unittest.mock import Mock

from sty.primitive import Register


def test_register_call_returns_empty_string_when_muted():
    register = Register()
    register.is_muted = True
    register.eightbit_call = Mock(side_effect=AssertionError("must not be called"))
    register.rgb_call = Mock(side_effect=AssertionError("must not be called"))

    assert register(42) == ""
    assert register(1, 2, 3) == ""
    register.eightbit_call.assert_not_called()
    register.rgb_call.assert_not_called()


def test_register_call_with_one_integer_uses_eightbit_renderer():
    register = Register()
    register.eightbit_call = Mock(return_value="eight-bit result")

    result = register(42, option="value")

    assert result == "eight-bit result"
    register.eightbit_call.assert_called_once_with(42, option="value")


def test_register_call_with_one_string_returns_named_attribute():
    register = Register()
    register.red = "rendered red"

    assert register("red") == "rendered red"


def test_register_call_with_three_arguments_uses_rgb_renderer():
    register = Register()
    register.rgb_call = Mock(return_value="rgb result")

    result = register(102, 49, 42, option="value")

    assert result == "rgb result"
    register.rgb_call.assert_called_once_with(102, 49, 42, option="value")


def test_register_call_with_unsupported_argument_counts_returns_empty_string():
    register = Register()
    register.eightbit_call = Mock(side_effect=AssertionError("must not be called"))
    register.rgb_call = Mock(side_effect=AssertionError("must not be called"))

    assert register() == ""
    assert register(1, 2) == ""
    assert register(1, 2, 3, 4) == ""
    register.eightbit_call.assert_not_called()
    register.rgb_call.assert_not_called()
