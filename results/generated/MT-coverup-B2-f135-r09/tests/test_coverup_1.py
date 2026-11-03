# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

import pytest

from f135 import can_arrange


def test_can_arrange_empty_list():
    """While-loop condition is False immediately (i=1 not < len=0)."""
    assert can_arrange([]) == -1


def test_can_arrange_single_element():
    """While-loop condition is False immediately (i=1 not < len=1)."""
    assert can_arrange([7]) == -1


def test_can_arrange_non_decreasing_returns_minus_one():
    """While-loop body runs but 'if' branch (arr[i] < arr[i-1]) is never True."""
    assert can_arrange([1, 2, 3, 4, 5]) == -1


def test_can_arrange_all_equal_returns_minus_one():
    """Equal neighbors do not satisfy the strict '<' comparison."""
    assert can_arrange([2, 2, 2]) == -1


def test_can_arrange_single_drop():
    """'if' branch True once, then False again; latest (largest) index returned."""
    assert can_arrange([1, 2, 4, 3, 5]) == 3


def test_can_arrange_multiple_drops_returns_last_index():
    """'if' branch True multiple times; the last (largest) drop index wins."""
    assert can_arrange([1, 5, 4, 3, 2]) == 4


def test_can_arrange_strictly_decreasing():
    """Every comparison after the first is True; result is len(arr)-1."""
    assert can_arrange([5, 4, 3, 2, 1]) == 4
