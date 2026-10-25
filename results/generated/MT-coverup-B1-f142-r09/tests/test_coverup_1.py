# file: project/f142/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}

import pytest

from f142 import sum_squares


def test_sum_squares_all_branches():
    # indices 0..8 exercise every branch:
    #   i % 3 == 0            -> i = 0, 3, 6  (squared)
    #   i % 4 == 0 and i%3!=0 -> i = 4, 8     (cubed)
    #   else                  -> i = 1, 2, 5, 7 (unchanged)
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = (1**2 + 2 + 3 + 4**2 + 5**3 + 6 + 7**2 + 8 + 9**3)
    assert expected == 939
    assert sum_squares(lst) == 939


def test_sum_squares_empty_list():
    assert sum_squares([]) == 0


def test_sum_squares_single_element_index_zero():
    # index 0 hits the i % 3 == 0 branch
    assert sum_squares([7]) == 49


def test_sum_squares_does_not_mutate_input():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    snapshot = list(lst)
    sum_squares(lst)
    assert lst == snapshot
