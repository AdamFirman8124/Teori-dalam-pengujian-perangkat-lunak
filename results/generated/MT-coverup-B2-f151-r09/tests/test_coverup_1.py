# file: project/f151/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f151 import double_the_difference


def test_double_the_difference_all_qualifying():
    """All elements are positive odd integers, so line 3 (the return) executes
    and every element contributes to the sum."""
    assert double_the_difference([1, 3, 5]) == 1 ** 2 + 3 ** 2 + 5 ** 2 == 35


def test_double_the_difference_covers_every_branch():
    """Exercises every short-circuit branch of the comprehension condition:
      - i > 0 False        (negative numbers and zero)
      - i % 2 != 0 False   (positive even integers)
      - '.' in str(i) True (positive odd floats such as 1.5 and 3.0)
      - all three True     (positive odd integers 1 and 7)
    """
    lst = [1, -3, 0, 2, 4, 1.5, 3.0, 7]
    # Only 1 and 7 qualify: 1**2 + 7**2 == 50
    assert double_the_difference(lst) == 50


def test_double_the_difference_no_qualifying_elements():
    """No element passes the filter, so the comprehension yields an empty list
    and sum() returns 0; the false branches are still exercised."""
    assert double_the_difference([-1, -2, 0, 2, 4, 1.5]) == 0


def test_double_the_difference_empty_list():
    """An empty input list still executes line 3 and returns 0."""
    assert double_the_difference([]) == 0
