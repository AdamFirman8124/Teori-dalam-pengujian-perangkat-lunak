# file: script_79.py:1-13
# asked: {"lines": [13], "branches": []}
# gained: {"lines": [13], "branches": []}

import pytest
from script_79 import decimal_to_binary


def test_decimal_to_binary_positive():
    """Test conversion of positive decimal numbers to binary."""
    assert decimal_to_binary(15) == "db1111db"
    assert decimal_to_binary(32) == "db100000db"
    assert decimal_to_binary(1) == "db1db"
    assert decimal_to_binary(7) == "db111db"


def test_decimal_to_binary_zero():
    """Test conversion of zero to binary."""
    assert decimal_to_binary(0) == "db0db"


def test_decimal_to_binary_large_number():
    """Test conversion of a large decimal number to binary."""
    assert decimal_to_binary(255) == "db11111111db"
    assert decimal_to_binary(1024) == "db10000000000db"


def test_decimal_to_binary_power_of_two():
    """Test conversion of powers of two to binary."""
    assert decimal_to_binary(2) == "db10db"
    assert decimal_to_binary(4) == "db100db"
    assert decimal_to_binary(8) == "db1000db"
    assert decimal_to_binary(16) == "db10000db"
    assert decimal_to_binary(64) == "db1000000db"
