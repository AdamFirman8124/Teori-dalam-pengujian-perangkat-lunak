# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import math

import pytest

from f133 import sum_squares


def test_sum_squares_non_empty_list():
    """Covers lines 3-7 with the loop body executed (loop branch taken)."""
    lst = [1.2, 2.5, -3.7]
    result = sum_squares(lst)
    expected = math.ceil(1.2) ** 2 + math.ceil(2.5) ** 2 + math.ceil(-3.7) ** 2
    # math.ceil(1.2) == 2, math.ceil(2.5) == 3, math.ceil(-3.7) == -3
    assert result == expected == 2 ** 2 + 3 ** 2 + (-3) ** 2 == 22
    # Postcondition: input list is not mutated by the function.
    assert lst == [1.2, 2.5, -3.7]


def test_sum_squares_empty_list():
    """Covers the loop-not-taken branch (lines 3, 4, 5, 7; line 6 skipped)."""
    assert sum_squares([]) == 0


def test_sum_squares_integers():
    """Covers the loop body with integer inputs (ceil is identity on ints)."""
    assert sum_squares([1, 2, 3]) == 1 + 4 + 9 == 14


def test_sum_squares_single_element():
    """Covers the loop body with exactly one iteration."""
    assert sum_squares([-0.5]) == math.ceil(-0.5) ** 2 == 0
