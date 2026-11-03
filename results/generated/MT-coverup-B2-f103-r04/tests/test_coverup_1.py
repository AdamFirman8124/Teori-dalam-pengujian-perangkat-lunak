# file: project/f103/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest

from f103 import rounded_avg


def test_rounded_avg_m_less_than_n_returns_minus_one():
    """Covers lines 3-4: the branch where m < n."""
    assert rounded_avg(5, 3) == -1


def test_rounded_avg_single_element_range():
    """Covers lines 5-8 with n == m (loop body runs once)."""
    # summation = 3, average = 3/1 = 3 -> bin(3) == '0b11'
    assert rounded_avg(3, 3) == "0b11"


def test_rounded_avg_multi_element_range():
    """Covers lines 5-8 with several loop iterations."""
    # summation of 1..5 = 15, average = 15/5 = 3 -> bin(3) == '0b11'
    assert rounded_avg(1, 5) == "0b11"


def test_rounded_avg_rounding_applied():
    """Covers lines 5-8 including the rounding of a fractional average."""
    # summation of 1..2 = 3, average = 3/2 = 1.5, round(1.5) == 2 -> '0b10'
    assert rounded_avg(1, 2) == "0b10"


def test_rounded_avg_negative_numbers():
    """Covers lines 5-8 with negative bounds."""
    # summation of -3..1 = -5, average = -5/5 = -1 -> bin(-1) == '-0b1'
    assert rounded_avg(-3, 1) == "-0b1"
