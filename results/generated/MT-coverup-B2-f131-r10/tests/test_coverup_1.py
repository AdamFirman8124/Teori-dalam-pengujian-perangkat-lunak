# file: project/f131/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}

import pytest

from f131 import digits


def test_digits_all_odd_digits_returns_product():
    # Covers lines 3-9 (init, loop, odd branch) and line 13 (return product).
    # 15 -> digits 1 and 5 are odd -> product = 1 * 1 * 5 = 5
    assert digits(15) == 5


def test_digits_mixed_digits_skips_even_digits():
    # Covers the False branch of the odd check (line 7) via even digits 2 and 4,
    # while odd digits 1 and 3 still update product/odd_count.
    # 1234 -> odd digits 1, 3 -> product = 1 * 3 = 3
    assert digits(1234) == 3


def test_digits_no_odd_digits_returns_zero():
    # Covers lines 10-11: odd_count == 0 -> return 0.
    # 2468 -> all digits even -> product never updated -> 0
    assert digits(2468) == 0


def test_digits_zero_returns_zero():
    # Single even digit (0) -> odd_count stays 0 -> returns 0.
    assert digits(0) == 0


def test_digits_single_odd_digit():
    # Single odd digit -> product equals that digit, exercises line 13 again.
    assert digits(7) == 7


def test_digits_product_of_multiple_odd_digits():
    # 359 -> odd digits 3, 5, 9 -> product = 3 * 5 * 9 = 135
    assert digits(359) == 135
