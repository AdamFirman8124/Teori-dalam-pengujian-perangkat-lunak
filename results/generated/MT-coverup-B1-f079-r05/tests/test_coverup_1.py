# file: project/f079/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f079 import decimal_to_binary


def test_decimal_to_binary_zero():
    assert decimal_to_binary(0) == "db0db"


def test_decimal_to_binary_one():
    assert decimal_to_binary(1) == "db1db"


def test_decimal_to_binary_five():
    assert decimal_to_binary(5) == "db101db"


def test_decimal_to_binary_ten():
    result = decimal_to_binary(10)
    assert result == "db1010db"
    assert result.startswith("db")
    assert result.endswith("db")
    assert result[2:-2] == bin(10)[2:]


def test_decimal_to_binary_fifteen():
    assert decimal_to_binary(15) == "db1111db"


def test_decimal_to_binary_large():
    assert decimal_to_binary(32) == "db100000db"
    assert decimal_to_binary(255) == "db11111111db"
    assert decimal_to_binary(1024) == "db10000000000db"
