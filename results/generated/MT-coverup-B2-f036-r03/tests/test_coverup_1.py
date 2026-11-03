# file: project/f036/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}

"""Tests for f036.fizz_buzz achieving full line and branch coverage.

fizz_buzz(n) collects every i in range(n) divisible by 11 or 13,
concatenates their decimal representations, and returns the number of
'7' digits in that string.

The function is pure (no I/O, no global state), so no monkeypatching or
teardown is required; each test is self-contained and leaves no state
behind.
"""

from f036 import fizz_buzz


def test_n_zero_skips_both_loops():
    """n = 0 exercises lines 3, 8, 11 plus the 'loop not entered'
    branches of the for-loops on lines 4 and 9 (s stays empty)."""
    assert fizz_buzz(0) == 0


def test_collects_multiples_without_sevens():
    """range(50) yields 0, 11, 13, 22, 26, 33, 39, 44 ->
    '011132226333944', which contains no '7'.

    Covers the loop body (line 6), the join (line 7), the counting loop
    entered (line 9) and the c == '7' False branch (line 10)."""
    assert fizz_buzz(50) == 0


def test_counts_seven_digits():
    """range(79) additionally contains 77 and 78, contributing three
    '7' digits. Covers the c == '7' True branch of line 10."""
    assert fizz_buzz(79) == 3


def test_boundary_78():
    """78 is the second collected number containing a '7': excluded
    when n == 78 (answer 2), included when n == 79 (answer 3)."""
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3


def test_second_or_operand_taken():
    """i = 13 makes 'i % 11 == 0' False but 'i % 13 == 0' True,
    covering the second operand of the 'or' on line 5; i = 1 covers
    the both-False branch. Collected '01113' has no '7'."""
    assert fizz_buzz(14) == 0


def test_single_element_collection():
    """n = 12 collects only 0 and 11 -> '011', returning 0; verifies
    the append path with a minimal non-trivial input."""
    assert fizz_buzz(12) == 0
