# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

import pytest

from f135 import can_arrange


def test_can_arrange_single_element_loop_not_entered():
    # len(arr) == 1 -> while loop body never runs; returns -1
    assert can_arrange([5]) == -1


def test_can_arrange_empty():
    # len(arr) == 0 -> while loop body never runs; returns -1
    assert can_arrange([]) == -1


def test_can_arrange_no_descending_pair():
    # loop runs, condition arr[i] < arr[i-1] always False -> ind stays -1
    assert can_arrange([1, 2, 3, 4]) == -1


def test_can_arrange_descending_pair_updates_ind():
    # loop runs, condition True at least once -> ind updated to last such index
    assert can_arrange([1, 2, 4, 3]) == 3


def test_can_arrange_last_descending_pair_wins():
    # multiple descending pairs: ind must be the index of the last one
    assert can_arrange([5, 4, 3, 2]) == 3


def test_can_arrange_equal_elements_not_descending():
    # equal neighbors: arr[i] < arr[i-1] is False, so ind stays -1
    assert can_arrange([2, 2, 2]) == -1
