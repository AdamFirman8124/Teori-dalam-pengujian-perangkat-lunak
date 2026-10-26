# file: project/f066/__init__.py:1-3
# asked: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}
# gained: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}

import pytest

from f066 import digitSum


def test_digit_sum_empty_string():
    """Line 2: empty string returns 0."""
    assert digitSum("") == 0


def test_digit_sum_all_uppercase():
    """Line 3: uppercase chars contribute their ord values."""
    assert digitSum("aBC") == ord("B") + ord("C")
    assert digitSum("A") == ord("A")


def test_digit_sum_mixed_case():
    """Line 3: lowercase chars contribute 0, uppercase contribute ord."""
    assert digitSum("aBcD") == ord("B") + ord("D")
    assert digitSum("hello") == 0


def test_digit_sum_digits_and_symbols():
    """Non-letter characters are not uppercase, so contribute 0."""
    assert digitSum("1!2@") == 0
    assert digitSum("Z9") == ord("Z")
