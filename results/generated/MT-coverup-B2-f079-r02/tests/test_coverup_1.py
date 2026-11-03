# file: project/f079/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f079 import decimal_to_binary


def test_decimal_to_binary_basic():
    """Covers line 3: the return statement, with a multi-bit positive number."""
    assert decimal_to_binary(15) == "db1111db"


def test_decimal_to_binary_zero():
    """bin(0)[2:] is '0', so zero must be wrapped as db0db."""
    assert decimal_to_binary(0) == "db0db"


def test_decimal_to_binary_one():
    assert decimal_to_binary(1) == "db1db"


def test_decimal_to_binary_power_of_two():
    """bin(32)[2:] strips the '0b' prefix, leaving '100000'."""
    assert decimal_to_binary(32) == "db100000db"


def test_decimal_to_binary_large():
    assert decimal_to_binary(103) == "db1100111db"


def test_decimal_to_binary_matches_bin():
    """Postcondition: result is exactly 'db' + binary digits + 'db'."""
    for n in (0, 1, 2, 7, 8, 255, 1024):
        result = decimal_to_binary(n)
        assert result.startswith("db")
        assert result.endswith("db")
        assert result[2:-2] == bin(n)[2:]
        assert set(result[2:-2]) <= {"0", "1"}
