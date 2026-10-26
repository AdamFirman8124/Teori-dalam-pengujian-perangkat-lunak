# file: project/f036/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}

import pytest

from f036 import fizz_buzz


def test_fizz_buzz_zero_range():
    # n = 0: loop body never runs, empty string, answer 0
    assert fizz_buzz(0) == 0


def test_fizz_buzz_no_sevens():
    # Multiples of 11 or 13 below 50 contain no digit '7'
    # ns = [0, 11, 13, 22, 26, 33, 39, 44] -> "011132226333944"
    assert fizz_buzz(50) == 0


def test_fizz_buzz_with_sevens():
    # Multiples of 11 or 13 below 78:
    # ns = [0, 11, 13, 22, 26, 33, 39, 44, 55, 65, 66, 77]
    # concatenated: "01113222633394455656677" -> two '7' digits (from 77)
    assert fizz_buzz(78) == 2


def test_fizz_buzz_negative_range():
    # Negative n: range(n) is empty, so result is 0
    assert fizz_buzz(-5) == 0


def test_fizz_buzz_single_multiple():
    # Only 0 is a multiple of 11 or 13 below 1
    assert fizz_buzz(1) == 0
