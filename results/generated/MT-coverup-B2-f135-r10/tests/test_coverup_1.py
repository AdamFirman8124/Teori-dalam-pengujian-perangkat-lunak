# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

"""Tests for f135.can_arrange — full line and branch coverage.

can_arrange(arr) returns the largest index i (>= 1) such that
arr[i] < arr[i-1], or -1 if the array is non-decreasing (or has
fewer than two elements).

Coverage plan:
- line 3 (ind=-1) / line 4 (i=1): executed by every call.
- line 5 (while): true branch via multi-element arrays,
  false branch via empty and single-element arrays.
- line 6 (if): true branch via arrays containing a descent,
  false branch via a strictly non-decreasing array.
- line 7 (ind=i): exercised whenever a descent is found.
- line 8 (i+=1): exercised on every loop iteration.
- line 9 (return): exercised by every call.
"""

import pytest

from f135 import can_arrange


def test_can_arrange_empty_list():
    """Empty input: while-condition (line 5) is false immediately."""
    assert can_arrange([]) == -1


def test_can_arrange_single_element():
    """Single element: loop body never runs, returns sentinel -1."""
    assert can_arrange([42]) == -1


def test_can_arrange_non_decreasing():
    """Loop runs (line 5 true) but the if (line 6) is never true."""
    assert can_arrange([1, 2, 2, 3]) == -1


def test_can_arrange_single_descent():
    """Exactly one descent: if-branch (line 6/7) taken once."""
    assert can_arrange([1, 2, 4, 3, 5]) == 3


def test_can_arrange_all_descending():
    """Every step descends: if-branch taken repeatedly, last index wins."""
    assert can_arrange([5, 4, 3, 2, 1]) == 4


def test_can_arrange_descent_then_ascent():
    """Descent followed by ascent: the earliest (largest) index is kept."""
    assert can_arrange([1, 3, 2, 4, 5]) == 2


def test_can_arrange_descent_at_end():
    """Descent occurs only at the final comparison."""
    assert can_arrange([1, 2, 3, 5, 4]) == 4


def test_can_arrange_descents_with_equal_neighbors():
    """Equal neighbors do not count as descents; only strict '<' does."""
    assert can_arrange([2, 2, 1, 1, 3]) == 2
