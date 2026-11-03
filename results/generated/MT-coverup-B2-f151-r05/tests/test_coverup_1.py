# file: project/f151/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f151 import double_the_difference


def test_sums_squares_of_positive_odd_integers():
    # Covers the case where all three conditions in the comprehension
    # filter evaluate to True (elements are kept and squared).
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25


def test_excludes_non_positive_numbers():
    # Covers the short-circuit branch where "i > 0" is False
    # (negative numbers and zero are skipped).
    assert double_the_difference([-1, -3, 0]) == 0


def test_excludes_even_numbers():
    # Covers the short-circuit branch where "i % 2 != 0" is False
    # (positive even numbers are skipped).
    assert double_the_difference([2, 4, 6]) == 0


def test_excludes_floats():
    # Covers the branch where '"." not in str(i)' is False
    # (floats whose string representation contains "." are skipped).
    assert double_the_difference([1.5, 3.5]) == 0


def test_excludes_even_valued_floats():
    # A float like 2.0 fails "i % 2 != 0" (2.0 % 2 == 0.0),
    # exercising the second condition with a float operand.
    assert double_the_difference([2.0]) == 0


def test_empty_list():
    # Line 3 must execute even for an empty input; sum of nothing is 0.
    assert double_the_difference([]) == 0


def test_mixed_list():
    # Exercises every branch of the filter in a single call:
    # 1   -> kept (1**2 = 1)
    # -2  -> fails "i > 0"
    # 2   -> fails "i % 2 != 0"
    # 1.5 -> fails '"." not in str(i)'
    # 3   -> kept (3**2 = 9)
    assert double_the_difference([1, -2, 2, 1.5, 3]) == 10
