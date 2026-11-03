# file: project/f066/__init__.py:1-3
# asked: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}
# gained: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}

import pytest

from f066 import digitSum


def test_digit_sum_empty_string():
    """Covers line 2: the empty-string early return."""
    assert digitSum("") == 0


def test_digit_sum_all_uppercase():
    """Covers line 3 with the isupper() == True branch."""
    # 'A' -> 65, 'B' -> 66, 'C' -> 67
    assert digitSum("ABC") == 65 + 66 + 67


def test_digit_sum_no_uppercase():
    """Covers line 3 with the isupper() == False branch."""
    assert digitSum("abc") == 0
    assert digitSum("123 !?") == 0


def test_digit_sum_mixed():
    """Covers line 3 with both branches of the conditional expression."""
    # Only uppercase characters contribute: 'a' -> 0, 'B' -> 66, '1' -> 0, 'C' -> 67
    assert digitSum("aB1C") == ord("B") + ord("C")
    assert digitSum("xY") == ord("Y")
