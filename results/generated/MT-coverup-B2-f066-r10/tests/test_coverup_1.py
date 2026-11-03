# file: project/f066/__init__.py:1-3
# asked: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}
# gained: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}

import pytest

from f066 import digitSum


def test_empty_string_returns_zero():
    """Covers line 2: the `if s == "": return 0` branch."""
    assert digitSum("") == 0


def test_all_uppercase_sums_ordinals():
    """Covers line 3 with the `char.isupper()` True branch."""
    assert digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert digitSum("Z") == ord("Z")


def test_all_lowercase_sums_zero():
    """Covers line 3 with the `else 0` branch (no uppercase chars)."""
    assert digitSum("abc") == 0
    assert digitSum("xyz") == 0


def test_mixed_case_counts_only_uppercase():
    """Covers both branches of the conditional expression on line 3."""
    assert digitSum("aBcD") == ord("B") + ord("D")
    assert digitSum("Hello World") == ord("H") + ord("W")


def test_non_alpha_characters_contribute_zero():
    """Digits, punctuation and whitespace are not upper, so contribute 0."""
    assert digitSum("1! Z") == ord("Z")
    assert digitSum("123!@#") == 0
