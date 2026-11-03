# file: project/f066/__init__.py:1-3
# asked: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}
# gained: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}

import pytest

from f066 import digitSum


def test_digit_sum_empty_string():
    """Covers line 2: the empty-string early return."""
    assert digitSum("") == 0


def test_digit_sum_all_uppercase():
    """Covers line 3 with char.isupper() True: sums ord() of uppercase chars."""
    assert digitSum("ABC") == ord("A") + ord("B") + ord("C") == 65 + 66 + 67


def test_digit_sum_all_lowercase():
    """Covers line 3 with char.isupper() False: contributes 0 for each char."""
    assert digitSum("abc") == 0


def test_digit_sum_mixed_case():
    """Covers both branches of the conditional expression on line 3."""
    assert digitSum("aBcD") == ord("B") + ord("D") == 66 + 68


def test_digit_sum_uppercase_with_spaces_and_digits():
    """Non-letter characters are not upper, so they contribute 0."""
    assert digitSum("A1 b!Z") == ord("A") + ord("Z") == 65 + 90


def test_digit_sum_single_uppercase_char():
    """Single uppercase character returns its ordinal value."""
    assert digitSum("H") == 72
