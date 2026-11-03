# file: project/f129/__init__.py:1-29
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}

"""Tests for f129.minPath covering all previously unexecuted lines 3-29.

minPath is a pure function (no globals, no I/O, no mutation of its inputs),
so no monkeypatching/cleanup is required; each test uses fresh local data
to avoid any state pollution between tests.
"""

import pytest

from f129 import minPath


def test_min_path_one_in_center_all_neighbor_branches_true():
    """1 at the center of a 3x3 grid: all four '!=' neighbor branches are True.

    Covers lines 3-8, 9-10 (i != 0), 12-13 (j != 0), 15-16 (i != n-1),
    18-19 (j != n-1), 21 (val = min(temp)), 23-29 (both parity branches).
    """
    grid = [
        [2, 2, 2],
        [2, 1, 2],
        [2, 2, 2],
    ]
    # k odd: even indices append 1, odd indices append val (= 2).
    assert minPath(grid, 3) == [1, 2, 1]
    # k even: exercises the else branch (line 28) on the last element too.
    assert minPath(grid, 4) == [1, 2, 1, 2]


def test_min_path_one_in_top_left_corner():
    """1 at (0, 0): 'i != 0' and 'j != 0' branches are False (skipped)."""
    grid = [
        [1, 2],
        [3, 4],
    ]
    # Neighbors found: down (3) and right (2) -> val = 2.
    assert minPath(grid, 4) == [1, 2, 1, 2]


def test_min_path_one_in_bottom_right_corner():
    """1 at (n-1, n-1): 'i != n-1' and 'j != n-1' branches are False (skipped)."""
    grid = [
        [2, 3],
        [4, 1],
    ]
    # Neighbors found: up (3) and left (4) -> val = 3.
    assert minPath(grid, 2) == [1, 3]


def test_min_path_no_one_in_grid():
    """No cell equals 1: the inner 'if' never fires and val stays n*n + 1."""
    grid = [
        [2, 2],
        [2, 2],
    ]
    # n = 2 -> initial val = 5 is used for odd positions.
    assert minPath(grid, 3) == [1, 5, 1]


def test_min_path_k_zero_returns_empty_list():
    """k == 0: the answer loop body (lines 25-28) never executes."""
    grid = [
        [1, 2],
        [2, 2],
    ]
    assert minPath(grid, 0) == []


def test_min_path_does_not_mutate_input():
    """Postcondition: the input grid is left untouched (no state pollution)."""
    grid = [
        [2, 2],
        [2, 1],
    ]
    snapshot = [row[:] for row in grid]
    minPath(grid, 3)
    assert grid == snapshot
