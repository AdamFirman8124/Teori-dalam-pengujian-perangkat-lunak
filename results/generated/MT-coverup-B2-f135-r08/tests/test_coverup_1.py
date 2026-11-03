# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

import pytest

from f135 import can_arrange


def test_can_arrange_empty():
    """Empty list: loop body never runs, returns -1."""
    assert can_arrange([]) == -1


def test_can_arrange_single_element():
    """Single element: loop condition fails immediately, returns -1."""
    assert can_arrange([7]) == -1


def test_can_arrange_no_descent():
    """Strictly increasing list: condition on line 6 never true, returns -1."""
    assert can_arrange([1, 2, 3, 4, 5]) == -1


def test_can_arrange_single_descent():
    """Exactly one descent: index of that descent is returned."""
    assert can_arrange([1, 2, 4, 3, 5]) == 3


def test_can_arrange_multiple_descents_returns_last():
    """Multiple descents: the largest such index wins (line 7 executed repeatedly)."""
    assert can_arrange([5, 4, 3, 2, 1]) == 4


def test_can_arrange_descent_at_end():
    """Descent occurring at the final position is still detected."""
    assert can_arrange([1, 2, 3, 2, 1]) == 4


def test_can_arrange_descending_then_ascending():
    """Descent early, then recovery: still returns the descent index."""
    assert can_arrange([3, 1, 2, 3, 4]) == 1
