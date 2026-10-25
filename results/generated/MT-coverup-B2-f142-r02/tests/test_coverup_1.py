# file: project/f142/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}

import pytest

from f142 import sum_squares


def test_sum_squares_all_branches():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    original = list(lst)

    # i=0 -> 1**2, i=1,2 -> unchanged, i=3 -> 4**2,
    # i=4 -> 5**3, i=5 -> unchanged, i=6 -> 7**2,
    # i=7 -> unchanged, i=8 -> 9**3
    expected = 1 + 2 + 3 + 16 + 125 + 6 + 49 + 8 + 729

    assert sum_squares(lst) == expected == 939
    assert lst == original  # input must not be mutated


def test_sum_squares_empty_list():
    assert sum_squares([]) == 0


def test_sum_squares_single_element_square_branch():
    assert sum_squares([5]) == 25


def test_sum_squares_cube_branch_only():
    # length 5 so index 4 is reached: 4 % 4 == 0 and 4 % 3 != 0
    assert sum_squares([0, 0, 0, 0, 2]) == 8


def test_sum_squares_else_branch_only():
    # indices 1 and 2 only hit the else branch
    assert sum_squares([0, 3, 4]) == 7
