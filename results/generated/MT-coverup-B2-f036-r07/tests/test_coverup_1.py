# file: project/f036/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}

"""Tests for f036.fizz_buzz (HumanEval #36).

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching or cleanup is required; each test simply calls it and
asserts the expected result.
"""

from f036 import fizz_buzz


def test_fizz_buzz_zero_n():
    """n = 0 -> empty range, empty string, answer 0 (covers loop-skip paths)."""
    assert fizz_buzz(0) == 0


def test_fizz_buzz_no_multiples():
    """n = 5 -> loop body runs but the condition is always False, so no
    numbers are collected and the answer is 0."""
    assert fizz_buzz(5) == 0


def test_fizz_buzz_multiples_without_seven():
    """n = 50 -> collects 0, 11, 13, 22, 26, 33, 39, 44; the concatenated
    string '011132226333944' contains no '7', so the answer is 0."""
    assert fizz_buzz(50) == 0


def test_fizz_buzz_counts_sevens():
    """n = 78 -> collected numbers include 77, whose two '7' digits are
    counted, giving 2."""
    assert fizz_buzz(78) == 2


def test_fizz_buzz_thirteen_branch():
    """n = 14 -> i = 13 exercises the 'i % 13 == 0' branch (i not divisible
    by 11); collected '01113' has no '7', so the answer is 0."""
    assert fizz_buzz(14) == 0


def test_fizz_buzz_eleven_branch():
    """n = 12 -> i = 11 exercises the 'i % 11 == 0' branch (i not divisible
    by 13); collected '011' has no '7', so the answer is 0."""
    assert fizz_buzz(12) == 0
