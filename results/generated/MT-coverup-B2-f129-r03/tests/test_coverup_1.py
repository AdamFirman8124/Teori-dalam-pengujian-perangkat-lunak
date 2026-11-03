# file: project/f129/__init__.py:1-29
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}

import pytest

from f129 import minPath


def test_min_path_no_one_present():
    """Value 1 absent from grid: `val` remains n*n + 1 and is used for odd steps."""
    grid = [[2, 2], [2, 2]]
    assert minPath(grid, 3) == [1, 5, 1]


def test_min_path_one_at_top_left():
    """Covers: i == 0 (skip up), j == 0 (skip left), i != n-1 (down), j != n-1 (right)."""
    grid = [[1, 3], [2, 4]]
    # val = min(grid[1][0]=2, grid[0][1]=3) = 2
    assert minPath(grid, 5) == [1, 2, 1, 2, 1]


def test_min_path_one_at_bottom_right():
    """Covers: i != 0 (up), j != 0 (left), i == n-1 (skip down), j == n-1 (skip right)."""
    grid = [[2, 3], [4, 1]]
    # val = min(grid[0][1]=3, grid[1][0]=4) = 3
    assert minPath(grid, 3) == [1, 3, 1]


def test_min_path_one_in_middle_of_3x3():
    """All four neighbor branches taken (up, left, down, right all appended)."""
    grid = [[2, 3, 4], [5, 1, 6], [7, 8, 9]]
    # val = min(3, 5, 8, 6) = 3
    assert minPath(grid, 2) == [1, 3]


def test_min_path_one_at_top_right():
    """Corners: i == 0 skip up, j != 0 take left, i != n-1 take down, j == n-1 skip right."""
    grid = [[3, 1], [2, 4]]
    # val = min(grid[0][0]=3, grid[1][1]=4) = 3
    assert minPath(grid, 2) == [1, 3]


def test_min_path_one_at_bottom_left():
    """Corners: i != 0 take up, j == 0 skip left, i == n-1 skip down, j != n-1 take right."""
    grid = [[3, 2], [1, 4]]
    # val = min(grid[0][0]=3, grid[1][1]=4) = 3
    assert minPath(grid, 2) == [1, 3]


def test_min_path_zero_steps():
    """k == 0: the answer-building loop body never executes."""
    assert minPath([[2]], 0) == []


def test_min_path_single_cell_without_one():
    """1x1 grid where the inner condition is false for the only cell."""
    assert minPath([[5]], 1) == [1]


def test_min_path_alternates_even_odd():
    """Even indices append 1, odd indices append val, for larger k."""
    grid = [[1, 9], [9, 9]]
    # val = min(grid[1][0]=9, grid[0][1]=9) = 9
    assert minPath(grid, 6) == [1, 9, 1, 9, 1, 9]
