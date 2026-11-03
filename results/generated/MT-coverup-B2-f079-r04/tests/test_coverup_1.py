# file: project/f079/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f079 import decimal_to_binary


def test_decimal_to_binary_single_bit():
    """Calling the function executes the return statement (line 3)."""
    result = decimal_to_binary(1)
    assert result == "db1db"


def test_decimal_to_binary_zero():
    result = decimal_to_binary(0)
    assert result == "db0db"


def test_decimal_to_binary_multi_bit():
    result = decimal_to_binary(10)
    assert result == "db1010db"


def test_decimal_to_binary_multiple_of_power_of_two():
    result = decimal_to_binary(15)
    assert result == "db1111db"


@pytest.mark.parametrize(
    "value,expected",
    [
        (0, "db0db"),
        (1, "db1db"),
        (2, "db10db"),
        (5, "db101db"),
        (255, "db11111111db"),
    ],
)
def test_decimal_to_binary_matches_bin_builtin(value, expected):
    """The result must be 'db' prefixed/suffixed binary digits of the input."""
    result = decimal_to_binary(value)
    assert result == "db" + bin(value)[2:] + "db"
    assert result == expected
    assert result.startswith("db")
    assert result.endswith("db")
    assert int(result[2:-2], 2) == value
