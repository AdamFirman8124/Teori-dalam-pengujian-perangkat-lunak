# file: project/f066/__init__.py:1-3
# asked: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}
# gained: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}

import pytest

from f066 import digitSum


def test_digit_sum_empty_string():
    """Covers line 2: the early return for the empty string."""
    assert digitSum("") == 0


def test_digit_sum_all_uppercase():
    """Covers line 3 with the char.isupper() branch taken."""
    # 'A' = 65, 'B' = 66, 'C' = 67
    assert digitSum("ABC") == 65 + 66 + 67


def test_digit_sum_all_lowercase():
    """Covers line 3 with the else branch (0) taken for every char."""
    assert digitSum("abc") == 0


def test_digit_sum_mixed_case():
    """Covers line 3 with both branches of the conditional expression."""
    # 'a' -> 0, 'B' -> 66, 'c' -> 0, 'D' -> 68
    assert digitSum("aBcD") == 66 + 68


def test_digit_sum_digits_and_symbols_are_ignored():
    """Non-uppercase characters (digits, punctuation, spaces) contribute 0."""
    assert digitSum("1! A") == ord("A")


def test_digit_sum_matches_reference_implementation():
    """Cross-check against an independent reference implementation."""
    for s in ["", "hello", "Hello, World!", "PYTHON", "pYtHoN 123"]:
        expected = sum(ord(c) for c in s if c.isupper())
        assert digitSum(s) == expected
