# file: project/f151/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f151 import double_the_difference


def test_double_the_difference_includes_positive_odd_integers():
    # Positive odd integers (no '.' in their string form) are squared and summed.
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25


def test_double_the_difference_filters_all_branches():
    # Exercise every branch of the comprehension condition:
    #   i > 0            -> False for 0, -1, -3 (short-circuits first check)
    #   i % 2 != 0       -> False for 2, 4 (short-circuits second check)
    #   '.' not in str(i)-> False for 1.5, 3.0 (short-circuits third check)
    lst = [1, 3, 2, 4, 0, -1, -3, 1.5, 3.0]
    # Only 1 and 3 qualify: 1**2 + 3**2 == 10
    assert double_the_difference(lst) == 10


def test_double_the_difference_empty_list():
    # Empty input still executes the return line and yields 0.
    assert double_the_difference([]) == 0


def test_double_the_difference_large_values():
    # Larger positive odd integers are handled correctly.
    assert double_the_difference([7, 9]) == 49 + 81
