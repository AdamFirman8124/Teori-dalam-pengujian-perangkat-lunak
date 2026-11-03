# file: project/f103/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest

from f103 import rounded_avg


def test_rounded_avg_returns_minus_one_when_m_less_than_n():
    """Covers the early-return branch (lines 3-4)."""
    assert rounded_avg(7, 5) == -1
    assert rounded_avg(0, -1) == -1


def test_rounded_avg_single_element_range():
    """Covers loop body executing exactly once (lines 5-8)."""
    # Average of [5, 5] is 5 -> bin(5) == '0b101'
    assert rounded_avg(5, 5) == "0b101"


def test_rounded_avg_multi_element_range():
    """Covers the loop accumulating multiple values (lines 5-8)."""
    # Average of 1..5 is 15/5 == 3 -> '0b11'
    assert rounded_avg(1, 5) == "0b11"
    # Average of 10..20 is 165/11 == 15 -> '0b1111'
    assert rounded_avg(10, 20) == "0b1111"
    # Average of 20..33 is 371/14 == 26.5 -> round -> 26 -> '0b11010'
    assert rounded_avg(20, 33) == "0b11010"


def test_rounded_avg_rounding_of_fractional_average():
    """Verifies rounding behavior on line 8 for non-integer averages."""
    # Average of 1..2 is 1.5 -> round(1.5) == 2 -> '0b10'
    assert rounded_avg(1, 2) == "0b10"
    # Average of 1..4 is 2.5 -> round(2.5) == 2 (banker's rounding) -> '0b10'
    assert rounded_avg(1, 4) == "0b10"


def test_rounded_avg_negative_range():
    """Covers the loop with negative bounds (lines 5-8)."""
    # Average of -5..-1 is -15/5 == -3 -> bin(-3) == '-0b11'
    assert rounded_avg(-5, -1) == "-0b11"
