# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

import pytest

from f135 import can_arrange


def test_can_arrange_finds_largest_descent_index():
    # Covers: while-loop body (line 5 true branch), the if-false branch
    # (i=1, i=2), the if-true branch (i=3, line 7), the increment (line 8),
    # and the loop-exit/return path (lines 5 false branch, line 9).
    assert can_arrange([1, 2, 4, 3, 5]) == 3


def test_can_arrange_no_descent_returns_minus_one():
    # Covers: while-loop body with the if condition always false (line 6
    # false branch), so ind stays -1; loop exit and return of -1.
    assert can_arrange([1, 2, 3]) == -1


def test_can_arrange_strictly_decreasing_returns_last_index():
    # Covers: the if-true branch taken on every iteration (line 7 executed
    # repeatedly), verifying the final (largest) index is returned.
    assert can_arrange([5, 4, 3, 2]) == 3


def test_can_arrange_empty_list():
    # Covers: while condition false on first evaluation (line 5 false
    # branch with no loop body), returning the initial -1.
    assert can_arrange([]) == -1


def test_can_arrange_single_element():
    # Covers: while condition false immediately (1 < 1 is False),
    # returning -1 without entering the loop body.
    assert can_arrange([7]) == -1


def test_can_arrange_descent_at_first_pair():
    # Covers: if-true branch at i=1 followed by if-false branches,
    # ensuring ind is not overwritten by later non-descents.
    assert can_arrange([3, 1, 2, 4]) == 1
