# file: project/f036/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}

import pytest

from f036 import fizz_buzz


def test_fizz_buzz_counts_sevens():
    # i in 0..49 divisible by 11 or 13: 0, 11, 13, 22, 26, 33, 39, 44
    # concatenated: "011132226333944" -> zero '7's
    assert fizz_buzz(50) == 0


def test_fizz_buzz_counts_sevens_positive():
    # i in 0..77 divisible by 11 or 13: 0,11,13,22,26,33,39,44,52,55,65,66,77
    # concatenated: "0111322263339445255656677" -> the trailing "77" gives two '7's
    assert fizz_buzz(78) == 2


def test_fizz_buzz_zero_n():
    # range(0) is empty: loop body (lines 4-6) skipped, s == '', second loop skipped
    assert fizz_buzz(0) == 0


def test_fizz_buzz_no_multiples():
    # n=11: only i=0 qualifies, s == '0', no 7s
    assert fizz_buzz(11) == 0


def test_fizz_buzz_multiple_sevens():
    # multiples of 11 or 13 below 118:
    # 0,11,13,22,26,33,39,44,52,55,65,66,77,78,88,91,99,104,110,117
    # digits containing 7: 77 -> two, 78 -> one, 117 -> one => total 4
    assert fizz_buzz(118) == 4
