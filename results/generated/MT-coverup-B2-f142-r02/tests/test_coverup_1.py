# file: project/f142/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}

import pytest

from f142 import sum_squares


def test_sum_squares_all_branches():
    """Exercise every branch: square (i%3==0), cube (i%4==0 and i%3!=0),
    plain value (else), plus i=12 where i%4==0 but i%3==0 (first branch wins)."""
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # i=0: 1**2=1, i=1: 2, i=2: 3, i=3: 4**2=16, i=4: 5**3=125, i=5: 6,
    # i=6: 7**2=49, i=7: 8, i=8: 9**3=729, i=9: 10**2=100, i=10: 11,
    # i=11: 12, i=12: 13**2=169 (12%3==0 so square, not cube)
    assert sum_squares(lst) == 1 + 2 + 3 + 16 + 125 + 6 + 49 + 8 + 729 + 100 + 11 + 12 + 169


def test_sum_squares_empty_list():
    """Line 3 and line 11 execute with an empty input; sum of nothing is 0."""
    assert sum_squares([]) == 0


def test_sum_squares_single_element():
    """Only index 0 exists: square branch taken, loop exits after one pass."""
    assert sum_squares([5]) == 25


def test_sum_squares_does_not_mutate_input():
    """Postcondition: the input list is left untouched (no state pollution)."""
    lst = [2, 3, 4]
    snapshot = list(lst)
    # i=0: 0%3==0 -> 2**2=4; i=1: else -> 3; i=2: else -> 4  => 4+3+4 = 11
    assert sum_squares(lst) == 11
    assert lst == snapshot
