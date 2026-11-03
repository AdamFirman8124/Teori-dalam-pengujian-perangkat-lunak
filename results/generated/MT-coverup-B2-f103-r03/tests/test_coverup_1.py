# file: project/f103/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest

from f103 import rounded_avg


def test_m_less_than_n_returns_minus_one():
    """Covers the 'm < n' branch evaluating to True (lines 3-4)."""
    result = rounded_avg(7, 5)
    assert result == -1
    assert isinstance(result, int)
    # Also with negative arguments
    assert rounded_avg(0, -3) == -1


def test_single_element_range():
    """Covers the loop body executing exactly once (lines 5-8)."""
    result = rounded_avg(5, 5)
    assert result == bin(5)
    assert result == "0b101"
    assert isinstance(result, str)


def test_basic_average():
    """Covers the loop accumulating several values (lines 6-7)."""
    # sum(1..5) = 15, average = 15 / 5 = 3
    result = rounded_avg(1, 5)
    assert result == bin(3)
    assert result == "0b11"


def test_rounding_behavior():
    """Covers the round() call on line 8 with fractional averages."""
    # sum(1..2) = 3, average = 1.5 -> banker's rounding gives 2
    assert rounded_avg(1, 2) == "0b10"
    # sum(0..1) = 1, average = 0.5 -> banker's rounding gives 0
    assert rounded_avg(0, 1) == "0b0"
    # sum(20..33) = 371, average = 26.5 -> banker's rounding gives 26
    assert rounded_avg(20, 33) == "0b11010"


def test_larger_range():
    """Covers a longer loop iteration (lines 6-7) and exact average."""
    # sum(10..20) = 165, count = 11, average = 15
    result = rounded_avg(10, 20)
    assert result == bin(15)
    assert result == "0b1111"


def test_negative_numbers():
    """Covers the loop and return with negative bounds (lines 5-8)."""
    # sum(-5..-1) = -15, count = 5, average = -3
    result = rounded_avg(-5, -1)
    assert result == bin(-3)
    assert result == "-0b11"


def test_zero_width_and_boundaries():
    """Edge cases around zero for both branches."""
    # m == n is not 'm < n', so it goes through the loop (line 3 False branch)
    assert rounded_avg(0, 0) == "0b0"
    # m just below n triggers the early return (line 3 True branch)
    assert rounded_avg(1, 0) == -1
