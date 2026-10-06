# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import pytest
from script_2 import truncate_number


def test_truncate_number_with_decimal():
    """Test truncate_number with a number that has a decimal part."""
    result = truncate_number(3.5)
    assert result == 0.5


def test_truncate_number_with_zero_decimal():
    """Test truncate_number with a whole number."""
    result = truncate_number(5.0)
    assert result == 0.0


def test_truncate_number_with_small_decimal():
    """Test truncate_number with a small decimal part."""
    result = truncate_number(1.25)
    assert result == 0.25


def test_truncate_number_with_large_number():
    """Test truncate_number with a large number."""
    result = truncate_number(100.75)
    assert result == 0.75


def test_truncate_number_less_than_one():
    """Test truncate_number with a number less than 1."""
    result = truncate_number(0.333)
    assert abs(result - 0.333) < 1e-9
