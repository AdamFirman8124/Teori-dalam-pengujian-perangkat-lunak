# file: project/f079/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f079 import decimal_to_binary


def test_decimal_to_binary_basic():
    """Covers line 3: converts a positive integer to its binary representation wrapped in 'db'."""
    assert decimal_to_binary(15) == "db1111db"


def test_decimal_to_binary_zero():
    """Edge case: zero converts to 'db0db'."""
    assert decimal_to_binary(0) == "db0db"


def test_decimal_to_binary_one():
    """Edge case: one converts to 'db1db'."""
    assert decimal_to_binary(1) == "db1db"


def test_decimal_to_binary_power_of_two():
    """Power of two yields a single '1' followed by zeros."""
    assert decimal_to_binary(32) == "db100000db"


def test_decimal_to_binary_large():
    """Larger value: 255 -> 11111111."""
    assert decimal_to_binary(255) == "db11111111db"
