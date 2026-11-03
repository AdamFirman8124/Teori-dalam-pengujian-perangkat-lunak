# file: project/f131/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}

import pytest

from f131 import digits


def test_digits_all_even_returns_zero():
    """Covers lines 3-7 (even branch), 10-11: no odd digits -> return 0."""
    assert digits(2468) == 0


def test_digits_zero_returns_zero():
    """Covers lines 3-7 (even branch for digit 0), 10-11: digit 0 is even -> return 0."""
    assert digits(0) == 0


def test_digits_all_odd_returns_product():
    """Covers lines 3-9 (odd branch) and 13: all odd digits -> product of odds."""
    assert digits(135) == 1 * 3 * 5


def test_digits_mixed_returns_product_of_odds():
    """Covers lines 3-9, 10 (False branch), 13: mixed digits -> product of odd digits only."""
    assert digits(1234) == 1 * 3


def test_digits_single_odd_digit():
    """Covers lines 3-9, 10 (False branch), 13: a single odd digit -> that digit."""
    assert digits(7) == 7


def test_digits_negative_number_raises_value_error():
    """Covers lines 3-6: the '-' sign in str(n) makes int('-') raise ValueError."""
    with pytest.raises(ValueError):
        digits(-246)
