# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

"""Tests for f135.can_arrange covering lines 3-9 and all branches."""

import pytest

from f135 import can_arrange


def test_can_arrange_with_descending_pair_covers_if_true_branch():
    # Loop runs (line 5 True), if-condition True at least once (lines 6-7),
    # increments (line 8), and returns via line 9.
    # Largest index i where arr[i] < arr[i-1] is 3 (value 3 < value 4).
    assert can_arrange([1, 2, 4, 3, 5]) == 3


def test_can_arrange_strictly_increasing_covers_if_false_branch():
    # Loop runs (line 5 True), if-condition always False (line 6 -> line 8),
    # so ind stays -1 and is returned (line 9).
    assert can_arrange([1, 2, 3]) == -1


def test_can_arrange_empty_list_skips_loop_body():
    # While condition is False immediately (line 5 -> line 9),
    # exercising the loop-exit branch without entering the body.
    assert can_arrange([]) == -1


def test_can_arrange_single_element_skips_loop_body():
    # Same as above with one element: while 1 < 1 is False.
    assert can_arrange([7]) == -1


def test_can_arrange_last_element_is_the_descent():
    # Descent occurs at the final comparison; loop still terminates normally.
    assert can_arrange([5, 4]) == 1


def test_can_arrange_picks_largest_matching_index():
    # Multiple descents: indices 1 (2<3) and 3 (1<4); the largest, 3, wins
    # because ind is overwritten on every matching iteration.
    assert can_arrange([3, 2, 4, 1]) == 3
