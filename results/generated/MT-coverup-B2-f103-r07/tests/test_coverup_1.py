# file: project/f103/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest

from f103 import rounded_avg


def test_rounded_avg_m_less_than_n_returns_minus_one():
    """Covers the early-return branch (lines 3-4) when m < n."""
    result = rounded_avg(7, 3)
    assert result == -1


def test_rounded_avg_n_equals_m_single_value():
    """Covers the loop body (lines 5-8) with a single-iteration range."""
    result = rounded_avg(5, 5)
    assert result == bin(5)
    assert result == "0b101"


def test_rounded_avg_normal_range():
    """Covers lines 5-8 with a multi-iteration loop."""
    # sum(20..33) = (20 + 33) * 14 / 2 = 371; 371/14 = 26.5 -> round -> 26
    result = rounded_avg(20, 33)
    assert result == bin(26)
    assert result == "0b11010"


def test_rounded_avg_zero_case():
    """Covers lines 5-8 with n == m == 0."""
    result = rounded_avg(0, 0)
    assert result == "0b0"


def test_rounded_avg_returns_string_on_success():
    """Postcondition: successful calls return a binary string, errors return int."""
    assert isinstance(rounded_avg(1, 10), str)
    assert isinstance(rounded_avg(10, 1), int)
