# file: project/f036/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}

import pytest

from f036 import fizz_buzz


def test_fizz_buzz_empty_range():
    """n=0: loops never execute; result must be 0."""
    assert fizz_buzz(0) == 0


def test_fizz_buzz_both_branches_of_condition():
    """n=2: i=0 satisfies (0 % 11 == 0), i=1 does not; no '7' digits yet."""
    assert fizz_buzz(2) == 0


def test_fizz_buzz_counts_sevens():
    """n=78: multiples of 11/13 up to 77; '77' contributes two '7' chars."""
    # Multiples: 0, 11, 13, 22, 26, 33, 39, 44, 52, 55, 65, 66, 77
    # Concatenated: "011132239445255656677" -> exactly two '7' characters.
    assert fizz_buzz(78) == 2
