# file: script_103.py:1-17
# asked: {"lines": [12, 13, 14, 15, 16, 17], "branches": [[12, 13], [12, 14], [15, 16], [15, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17], "branches": [[12, 13], [12, 14], [15, 16], [15, 17]]}

import pytest
from script_103 import rounded_avg


def test_rounded_avg_n_greater_than_m():
    """Test that function returns -1 when n > m."""
    result = rounded_avg(7, 5)
    assert result == -1


def test_rounded_avg_single_number():
    """Test average when n equals m."""
    result = rounded_avg(5, 5)
    assert result == "0b101"


def test_rounded_avg_small_range():
    """Test average of integers from 1 to 5."""
    result = rounded_avg(1, 5)
    assert result == "0b11"


def test_rounded_avg_larger_range():
    """Test average of integers from 10 to 20."""
    result = rounded_avg(10, 20)
    assert result == "0b1111"


def test_rounded_avg_another_range():
    """Test average of integers from 20 to 33."""
    result = rounded_avg(20, 33)
    assert result == "0b11010"


def test_rounded_avg_two_consecutive_numbers():
    """Test average of two consecutive numbers."""
    result = rounded_avg(10, 11)
    assert result == "0b1010"


def test_rounded_avg_large_numbers():
    """Test with larger numbers to verify summation logic."""
    result = rounded_avg(100, 110)
    assert result == "0b1101001"
