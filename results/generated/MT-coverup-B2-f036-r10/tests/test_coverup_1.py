# file: project/f036/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}

"""Tests for f036.fizz_buzz covering all lines and branches (lines 3-11)."""

from f036 import fizz_buzz


def test_fizz_buzz_zero_range():
    """n=0: loop bodies never run; covers lines 3, 4, 7, 8, 11 (empty branches)."""
    assert fizz_buzz(0) == 0


def test_fizz_buzz_no_sevens():
    """n=50: exercises both branches of the if (i=0 true, i=1 false),
    the append, the join, and the char loop where every comparison is False."""
    # Multiples of 11 or 13 below 50: 0, 11, 13, 22, 26, 33, 39, 44 -> "011132226333944"
    # contains no '7'.
    assert fizz_buzz(50) == 0


def test_fizz_buzz_with_sevens():
    """n=78/79: char loop accumulates True comparisons (line 10 True branch)."""
    # Below 78: ..., 66, 77 -> "77" contributes two '7's.
    assert fizz_buzz(78) == 2
    # Below 79: additionally 78 -> one more '7'.
    assert fizz_buzz(79) == 3


def test_fizz_buzz_short_circuit_branches():
    """Covers the short-circuit arms of the 'or' on line 5:
    i=11 (first true, second skipped), i=13 (first false, second true),
    i=1 (both false)."""
    # 11 and 13 are both collected; 1 is not.
    assert fizz_buzz(14) == 0
