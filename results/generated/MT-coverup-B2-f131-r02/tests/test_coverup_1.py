# file: project/f131/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}

import pytest

from f131 import digits


def test_digits_no_odd_digits_returns_zero():
    """Covers loop over digits, even-digit branch (line 7 False),
    odd_count == 0 branch (line 10 True) and return 0 (line 11)."""
    assert digits(0) == 0
    assert digits(4) == 0
    assert digits(2468) == 0
    assert digits(24680) == 0


def test_digits_single_odd_digit_returns_itself():
    """Covers odd-digit branch (line 7 True), product update (line 8),
    odd_count increment (line 9) and return product (line 13)."""
    assert digits(1) == 1
    assert digits(3) == 3
    assert digits(9) == 9


def test_digits_multiple_odd_digits_returns_product():
    """Covers repeated execution of lines 8-9 across loop iterations."""
    assert digits(235) == 15          # 3 * 5
    assert digits(13579) == 945       # 1 * 3 * 5 * 7 * 9
    assert digits(111) == 1           # 1 * 1 * 1


def test_digits_mixed_even_and_odd_digits_returns_product_of_odd():
    """Covers both branches of line 7 within a single call, and the
    odd_count != 0 branch of line 10 leading to return product."""
    assert digits(123456) == 15       # 1 * 3 * 5
    assert digits(2468135) == 15      # 1 * 3 * 5
    assert digits(10203040) == 3      # 3


def test_digits_result_is_always_nonzero_when_odd_digits_present():
    """Postcondition: result is a positive product of odd digits."""
    result = digits(987654321)
    assert result == 945              # 9 * 7 * 5 * 3 * 1
    assert result > 0
