# file: project/f103/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest

from f103 import rounded_avg


def test_rounded_avg_returns_minus_one_when_m_less_than_n():
    """Covers line 4: the early-return branch when m < n."""
    assert rounded_avg(5, 3) == -1
    assert rounded_avg(10, 0) == -1


def test_rounded_avg_computes_binary_average():
    """Covers lines 5-8: summation loop and binary conversion.

    rounded_avg(1, 5): sum = 1+2+3+4+5 = 15, count = 5, avg = 3.0
    -> bin(3) == '0b11'
    """
    assert rounded_avg(1, 5) == "0b11"


def test_rounded_avg_single_element_range():
    """Covers lines 5-8 with a single-iteration loop (n == m).

    rounded_avg(3, 3): sum = 3, count = 1, avg = 3.0 -> bin(3) == '0b11'
    """
    assert rounded_avg(3, 3) == "0b11"


def test_rounded_avg_rounds_half_to_even():
    """Covers lines 5-8 exercising the rounding behavior.

    rounded_avg(1, 4): sum = 10, count = 4, avg = 2.5
    Python's round() uses banker's rounding, so round(2.5) == 2
    -> bin(2) == '0b10'
    """
    assert rounded_avg(1, 4) == "0b10"


def test_rounded_avg_rounds_down_to_zero():
    """Covers lines 5-8 with a result rounding down to zero.

    rounded_avg(0, 1): sum = 1, count = 2, avg = 0.5
    round(0.5) == 0 (banker's rounding) -> bin(0) == '0b0'
    """
    assert rounded_avg(0, 1) == "0b0"
