# file: project/f103/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

"""Tests for f103.rounded_avg covering all lines and branches.

rounded_avg is a pure function (no I/O, no global state, no side effects),
so no monkeypatching or teardown is required to avoid state pollution.
"""

import pytest

from f103 import rounded_avg


def test_m_less_than_n_returns_minus_one():
    """Covers lines 3-4: the early-exit branch when m < n."""
    assert rounded_avg(7, 5) == -1
    assert rounded_avg(20, 10) == -1
    assert rounded_avg(0, -1) == -1


def test_single_element_range():
    """Covers lines 5-8 with a range of exactly one element (n == m)."""
    # summation = 5, average = 5/1 = 5.0 -> bin(5) == '0b101'
    assert rounded_avg(5, 5) == "0b101"


def test_average_is_exact_integer():
    """Covers lines 5-8 with an exact (non-rounding) average."""
    # summation = 1+2+3+4+5 = 15, average = 15/5 = 3.0 -> bin(3) == '0b11'
    assert rounded_avg(1, 5) == "0b11"


def test_larger_range_exact_average():
    """Covers lines 5-8 over a longer loop iteration."""
    # summation = sum(10..20) = 165, average = 165/11 = 15.0 -> '0b1111'
    assert rounded_avg(10, 20) == "0b1111"


def test_average_rounds_up():
    """Covers lines 5-8 where round() changes the value upward."""
    # summation = 1+2 = 3, average = 3/2 = 1.5, round(1.5) = 2 -> '0b10'
    assert rounded_avg(1, 2) == "0b10"


def test_average_rounds_down_bankers_rounding():
    """Covers lines 5-8 where round() rounds to the nearest even integer."""
    # summation = 0+1 = 1, average = 0.5, round(0.5) = 0 -> '0b0'
    assert rounded_avg(0, 1) == "0b0"
    # summation = 2+3 = 5, average = 2.5, round(2.5) = 2 -> '0b10'
    assert rounded_avg(2, 3) == "0b10"


def test_negative_range():
    """Covers lines 5-8 with negative operands and a negative result."""
    # summation = -3 + -2 + -1 + 0 = -6, average = -6/4 = -1.5,
    # round(-1.5) = -2 (nearest even) -> bin(-2) == '-0b10'
    assert rounded_avg(-3, 0) == "-0b10"


@pytest.mark.parametrize(
    "n, m, expected",
    [
        (7, 5, -1),          # branch: m < n
        (5, 5, "0b101"),     # single element
        (1, 5, "0b11"),      # exact average
        (1, 2, "0b10"),      # rounds up
        (0, 1, "0b0"),       # rounds down (to even)
        (-3, 0, "-0b10"),    # negative range
        (10, 20, "0b1111"),  # longer loop
    ],
)
def test_rounded_avg_parametrized(n, m, expected):
    """Full-coverage parametrized check of every line and branch."""
    assert rounded_avg(n, m) == expected
