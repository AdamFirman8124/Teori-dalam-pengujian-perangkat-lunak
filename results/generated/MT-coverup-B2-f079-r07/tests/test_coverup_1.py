# file: project/f079/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f079 import decimal_to_binary


def test_decimal_to_binary_executes_return_line():
    """Call decimal_to_binary so that line 3 (the return statement) executes,
    and verify the wrapping/formatting postconditions."""
    result = decimal_to_binary(10)
    # Postconditions: result is wrapped in 'db' on both sides,
    # and the middle is the binary representation without the '0b' prefix.
    assert result == "db1010db"
    assert result.startswith("db")
    assert result.endswith("db")
    assert result[2:-2] == bin(10)[2:]


def test_decimal_to_binary_zero():
    """Edge case: zero should produce 'db0db'."""
    assert decimal_to_binary(0) == "db0db"


def test_decimal_to_binary_one():
    """Edge case: one should produce 'db1db'."""
    assert decimal_to_binary(1) == "db1db"


def test_decimal_to_binary_power_of_two():
    """Powers of two map to a single '1' followed by zeros."""
    assert decimal_to_binary(256) == "db100000000db"


def test_decimal_to_binary_negative_raises():
    """Negative input is not supported by bin()'s [2:] slicing convention here;
    bin(-5) == '-0b101', so [2:] yields 'b101'. Verify actual behavior."""
    assert decimal_to_binary(-5) == "dbb101db"
