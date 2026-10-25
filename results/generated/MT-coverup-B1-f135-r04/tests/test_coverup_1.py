# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

import pytest

from f135 import can_arrange


def test_can_arrange_empty_list_returns_minus_one():
    assert can_arrange([]) == -1


def test_can_arrange_single_element_returns_minus_one():
    assert can_arrange([5]) == -1


def test_can_arrange_sorted_list_returns_minus_one():
    # Loop runs, but the `arr[i] < arr[i - 1]` branch is never taken.
    assert can_arrange([1, 2, 3, 4]) == -1


def test_can_arrange_returns_index_of_last_decreasing_pair():
    assert can_arrange([1, 3, 2]) == 2


def test_can_arrange_multiple_decreases_returns_last_index():
    assert can_arrange([3, 2, 1]) == 2


def test_can_arrange_does_not_mutate_input():
    arr = [1, 3, 2]
    original = list(arr)
    can_arrange(arr)
    assert arr == original
