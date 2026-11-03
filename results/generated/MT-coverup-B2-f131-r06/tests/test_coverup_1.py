# file: project/f131/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}

"""Tests for f131.digits.

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching or fixture-based cleanup is required; there is no
state to pollute.

Coverage plan:
- lines 3-4 (initialization), 5-6 (loop over digits): exercised by every test
- line 7 true branch + lines 8-9 (odd digit accumulates product/count):
  test_digits_all_odd_digits, test_digits_mixed_digits,
  test_digits_single_odd_digit
- line 7 false branch (even digit skipped): test_digits_no_odd_digits,
  test_digits_mixed_digits, test_digits_zero, test_digits_even_only
- line 10 true branch + line 11 (return 0 when no odd digits):
  test_digits_no_odd_digits, test_digits_zero, test_digits_even_only
- line 10 false branch + line 13 (return product):
  test_digits_all_odd_digits, test_digits_mixed_digits,
  test_digits_single_odd_digit
"""

import pytest

from f131 import digits


def test_digits_all_odd_digits():
    """Every digit is odd: product of all odd digits is returned."""
    assert digits(135) == 1 * 3 * 5


def test_digits_mixed_digits():
    """Mix of odd and even digits: only odd digits contribute to the product."""
    assert digits(123) == 1 * 3


def test_digits_single_odd_digit():
    """A single odd digit: product equals that digit."""
    assert digits(7) == 7


def test_digits_no_odd_digits():
    """No odd digits at all: returns 0."""
    assert digits(248) == 0


def test_digits_zero():
    """Zero has no odd digits: returns 0."""
    assert digits(0) == 0


def test_digits_even_only_returns_zero_not_product():
    """Even-only input must return 0, not the initial product value of 1."""
    assert digits(2) == 0
