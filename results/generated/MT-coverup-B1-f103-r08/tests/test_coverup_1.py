# file: project/f103/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest

from f103 import rounded_avg


def test_rounded_avg_m_less_than_n_returns_minus_one():
    # Covers lines 3-4: the early-return branch when m < n.
    assert rounded_avg(5, 3) == -1
    assert rounded_avg(10, 0) == -1


def test_rounded_avg_normal_case():
    # Covers lines 5-8: summation loop and binary conversion of the rounded average.
    # Average of 1..4 is 2.5 -> round() uses banker's rounding -> 2 -> '0b10'
    assert rounded_avg(1, 4) == "0b10"
    # Average of 20..33 is 26.5 -> banker's rounding -> 26 -> '0b11010'
    assert rounded_avg(20, 33) == "0b11010"
    # Single-element range: average of 7..7 is 7 -> '0b111'
    assert rounded_avg(7, 7) == "0b111"
    # Negative numbers: average of -3..1 is -1 -> '0b-0x1' style output of bin(-1)
    assert rounded_avg(-3, 1) == bin(-1)
