# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

import pytest

from f135 import can_arrange


def test_no_descent_returns_minus_one():
    """Strictly increasing array: loop runs, condition (line 6) is always
    False, so line 7 is never taken and -1 is returned."""
    assert can_arrange([1, 2, 3]) == -1
    assert can_arrange([1, 1, 1]) == -1  # equal neighbours are not a descent


def test_descent_returns_last_index():
    """Array containing a descent: the True branch (lines 6-7) executes and
    the largest such index is returned."""
    assert can_arrange([1, 2, 4, 3, 5]) == 3
    # Two descents exist (indices 2 and 3); the later one must win.
    assert can_arrange([3, 1, 4, 1, 5]) == 3


def test_fully_descending_array():
    """Every comparison is a descent, so the final index is returned."""
    assert can_arrange([5, 4, 3, 2, 1]) == 4


def test_short_arrays_skip_loop_body():
    """For empty and single-element arrays the while condition (line 5) is
    False on the first check, so the loop body (lines 6-8) never runs."""
    assert can_arrange([]) == -1
    assert can_arrange([7]) == -1
