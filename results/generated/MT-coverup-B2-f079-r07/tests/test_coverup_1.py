# file: project/f079/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f079 import decimal_to_binary


def test_decimal_to_binary_positive():
    assert decimal_to_binary(15) == "db1111db"


def test_decimal_to_binary_zero():
    assert decimal_to_binary(0) == "db0db"


def test_decimal_to_binary_one():
    assert decimal_to_binary(1) == "db1db"


def test_decimal_to_binary_large():
    assert decimal_to_binary(32) == "db100000db"


def test_decimal_to_binary_negative():
    # bin(-1) == '-0b1' -> [2:] == 'b1'
    assert decimal_to_binary(-1) == "dbb1db"


def test_decimal_to_binary_returns_str_and_wraps():
    result = decimal_to_binary(6)
    assert isinstance(result, str)
    assert result.startswith("db")
    assert result.endswith("db")
    assert result[2:-2] == bin(6)[2:]
