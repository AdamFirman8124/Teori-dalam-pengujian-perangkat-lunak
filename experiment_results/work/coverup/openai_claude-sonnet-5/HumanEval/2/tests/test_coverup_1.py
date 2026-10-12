# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import pytest
from script_2 import truncate_number


def test_truncate_number_positive_decimal():
    """Test truncate_number with a positive number having decimal part."""
    result = truncate_number(3.5)
    assert result == 0.5


def test_truncate_number_integer():
    """Test truncate_number with an integer (no decimal part)."""
    result = truncate_number(5.0)
    assert result == 0.0


def test_truncate_number_small_decimal():
    """Test truncate_number with a small decimal value."""
    result = truncate_number(0.75)
    assert result == 0.75


def test_truncate_number_large_number():
    """Test truncate_number with a large number."""
    result = truncate_number(123.456)
    assert abs(result - 0.456) < 1e-9


def test_truncate_number_very_small_decimal():
    """Test truncate_number with very small decimal part."""
    result = truncate_number(10.001)
    assert abs(result - 0.001) < 1e-9
