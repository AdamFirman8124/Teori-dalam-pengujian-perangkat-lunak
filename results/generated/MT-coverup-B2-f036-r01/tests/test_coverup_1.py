# file: project/f036/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}

from f036 import fizz_buzz


def test_fizz_buzz_zero_range():
    # n = 0: range(0) is empty, so no numbers are collected and the
    # digit-counting loop never runs; the result must be 0.
    assert fizz_buzz(0) == 0


def test_fizz_buzz_small_range_hits_both_condition_branches():
    # n = 2: i=0 satisfies (0 % 11 == 0) -> appended;
    #        i=1 satisfies neither (1 % 11 != 0 and 1 % 13 != 0) -> skipped.
    # The collected string is "0", which contains no '7'.
    assert fizz_buzz(2) == 0


def test_fizz_buzz_no_sevens_below_50():
    # Multiples of 11 or 13 below 50 are:
    # 0, 11, 13, 22, 26, 33, 39, 44 -> "011132226333944" has no '7'.
    assert fizz_buzz(50) == 0


def test_fizz_buzz_counts_sevens_from_77():
    # Below 78, 77 (multiple of 11) contributes two '7' digits.
    assert fizz_buzz(78) == 2


def test_fizz_buzz_counts_sevens_from_77_and_78():
    # Below 79, 77 contributes two '7's and 78 (multiple of 13) one more.
    assert fizz_buzz(79) == 3


def test_fizz_buzz_larger_range_and_return_type():
    # Below 100 the qualifying numbers are
    # 0, 11, 13, 22, 26, 33, 39, 44, 52, 55, 65, 66, 77, 78, 88, 91, 99,
    # whose digits contain exactly three '7's (two in 77, one in 78).
    result = fizz_buzz(100)
    assert isinstance(result, int)
    assert result == 3
