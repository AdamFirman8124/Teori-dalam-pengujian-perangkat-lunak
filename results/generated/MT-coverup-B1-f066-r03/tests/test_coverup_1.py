# file: project/f066/__init__.py:1-3
# asked: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}
# gained: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}

import pytest

from f066 import digitSum


def test_digit_sum_empty_string():
    assert digitSum("") == 0


def test_digit_sum_all_uppercase():
    assert digitSum("ABC") == ord("A") + ord("B") + ord("C")


def test_digit_sum_all_lowercase():
    assert digitSum("abc") == 0


def test_digit_sum_mixed_case():
    assert digitSum("aBcD") == ord("B") + ord("D")


def test_digit_sum_with_non_letters():
    assert digitSum("A1b!") == ord("A")
