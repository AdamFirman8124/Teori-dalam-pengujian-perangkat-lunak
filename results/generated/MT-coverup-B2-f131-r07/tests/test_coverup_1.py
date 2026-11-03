# file: project/f131/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}

import pytest

from f131 import digits


def test_digits_with_odd_digits_returns_product():
    """Covers lines 3-9 and 13: loop over digits, odd-digit branch, final return of product."""
    # 235 -> odd digits are 3 and 5 -> product = 3 * 5 = 15
    assert digits(235) == 15
    # 1 -> single odd digit -> product = 1
    assert digits(1) == 1
    # 15 -> odd digits 1 and 5 -> product = 5
    assert digits(15) == 5
    # 999 -> product = 9 * 9 * 9 = 729
    assert digits(999) == 729


def test_digits_without_odd_digits_returns_zero():
    """Covers lines 3-7, 10-11: loop with only even digits, odd_count == 0 branch."""
    # 4 -> single even digit -> no odd digits -> 0
    assert digits(4) == 0
    # 2468 -> all even digits -> 0
    assert digits(2468) == 0
    # 0 -> digit 0 is even -> 0
    assert digits(0) == 0


def test_digits_mixed_digits():
    """Covers both branches of the parity check within a single call (lines 7-9 taken and skipped)."""
    # 1234 -> odd digits 1 and 3 -> product = 3, even digits skipped
    assert digits(1234) == 3
    # 20 -> odd digit 1 absent, only 2 and 0 -> 0
    assert digits(20) == 0
