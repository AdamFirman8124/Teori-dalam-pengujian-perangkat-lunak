# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

import pytest

from f135 import can_arrange


def test_can_arrange_empty_list():
    """Empty list: loop never runs, returns -1."""
    assert can_arrange([]) == -1


def test_can_arrange_single_element():
    """Single element: loop never runs, returns -1."""
    assert can_arrange([5]) == -1


def test_can_arrange_strictly_increasing():
    """No element smaller than its predecessor: returns -1."""
    assert can_arrange([1, 2, 3, 4, 5]) == -1


def test_can_arrange_decrease_at_end():
    """Decrease exists: returns the largest index i with arr[i] < arr[i-1]."""
    assert can_arrange([1, 2, 4, 3, 5]) == 3


def test_can_arrange_multiple_decreases_returns_last():
    """Multiple decreases: the last one wins (ind is overwritten)."""
    assert can_arrange([5, 4, 3, 2, 1]) == 4


def test_can_arrange_does_not_mutate_input():
    """Postcondition: input list is not modified."""
    arr = [3, 1, 2]
    snapshot = list(arr)
    can_arrange(arr)
    assert arr == snapshot
