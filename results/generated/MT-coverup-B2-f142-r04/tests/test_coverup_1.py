# file: project/f142/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 7], [7, 8], [7, 10]]}

import pytest

from f142 import sum_squares


def test_sum_squares_empty_list():
    """Covers function entry, loop over empty range, and return of sum([]) == 0."""
    assert sum_squares([]) == 0


def test_sum_squares_all_branches_short_list():
    """A 5-element list covers indices 0-4:
    i=0: i % 3 == 0        -> square
    i=1,2: else            -> unchanged
    i=3: i % 3 == 0        -> square
    i=4: i % 4 == 0 and i % 3 != 0 -> cube
    """
    lst = [1, 2, 3, 4, 5]
    expected = 1**2 + 2 + 3 + 4**2 + 5**3  # 1 + 2 + 3 + 16 + 125 = 147
    assert sum_squares(lst) == expected


def test_sum_squares_long_list_all_branches():
    """A 13-element list additionally covers i=12 (i % 4 == 0 but i % 3 == 0,
    so the elif's second condition is False and the first branch applies),
    exercising every branch of the if/elif/else chain."""
    lst = list(range(13))
    expected = (
        0**2    # i=0  (i % 3 == 0)
        + 1     # i=1  (else)
        + 2     # i=2  (else)
        + 3**2  # i=3  (i % 3 == 0)
        + 4**3  # i=4  (i % 4 == 0 and i % 3 != 0)
        + 5     # i=5  (else)
        + 6**2  # i=6  (i % 3 == 0)
        + 7     # i=7  (else)
        + 8**3  # i=8  (i % 4 == 0 and i % 3 != 0)
        + 9**2  # i=9  (i % 3 == 0)
        + 10    # i=10 (else)
        + 11    # i=11 (else)
        + 12**2 # i=12 (i % 3 == 0, even though i % 4 == 0 too)
    )
    assert sum_squares(lst) == expected  # 882


def test_sum_squares_does_not_mutate_input():
    """Postcondition: the input list is left untouched (function is pure)."""
    lst = [1, 2, 3, 4, 5]
    snapshot = list(lst)
    sum_squares(lst)
    assert lst == snapshot
