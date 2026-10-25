# file: project/f066/__init__.py:1-3
# asked: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}
# gained: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}

import pytest

from f066 import digitSum


def test_digit_sum_empty_string():
    """Covers lines 2-3: the empty-string early return."""
    assert digitSum("") == 0


def test_digit_sum_mixed_case():
    """Covers the generator expression: uppercase chars contribute ord(), others 0."""
    assert digitSum("aA") == ord("A")
    assert digitSum("Hello World") == ord("H") + ord("W")
    assert digitSum("abc") == 0
    assert digitSum("ABC") == ord("A") + ord("B") + ord("C")


def test_digit_sum_non_letter_characters():
    """Digits, punctuation and whitespace are not uppercase, so contribute 0."""
    assert digitSum("1! A") == ord("A")
    assert digitSum(" \t\n") == 0
