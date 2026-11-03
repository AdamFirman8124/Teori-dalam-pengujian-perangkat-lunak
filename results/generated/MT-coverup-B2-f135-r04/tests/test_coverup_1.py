# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

import pytest

from f135 import can_arrange


def test_can_arrange_fewer_than_two_elements():
    """With 0 or 1 elements the while-loop condition is immediately false,
    so lines 3, 4, 5 (false branch) and 9 execute and -1 is returned."""
    assert can_arrange([]) == -1
    assert can_arrange([42]) == -1


def test_can_arrange_no_descent():
    """Non-decreasing array: the loop body runs (lines 5, 6, 8) but the
    if-condition on line 6 is never true, so line 7 is skipped and -1 is returned."""
    assert can_arrange([1, 2, 3, 4, 5]) == -1
    assert can_arrange([2, 2, 2]) == -1


def test_can_arrange_single_descent():
    """Exactly one descent: line 6 takes the true branch and line 7 executes."""
    assert can_arrange([1, 2, 4, 3]) == 3
    assert can_arrange([5, 4]) == 1


def test_can_arrange_multiple_descents_returns_last_index():
    """Several descents: the function keeps updating ind (line 7) and returns
    the largest index i such that arr[i] < arr[i-1]."""
    assert can_arrange([4, 8, 5, 7, 3]) == 4
    assert can_arrange([10, 9, 8, 7]) == 3
