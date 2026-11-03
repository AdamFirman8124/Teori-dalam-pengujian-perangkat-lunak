# file: project/f129/__init__.py:1-29
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}

"""Tests for f129.minPath that execute all previously uncovered lines (3-29)
and every branch of the function.

minPath is a pure function (no globals, files, or other external state are
touched), so no monkeypatching/teardown is required to avoid state pollution.
"""

from f129 import minPath


def test_min_path_one_in_center_hits_all_four_neighbor_branches():
    """1 in the middle of a 3x3 grid: all four neighbour 'if' branches are True."""
    grid = [
        [5, 6, 7],
        [8, 1, 2],
        [3, 4, 9],
    ]
    # Neighbours of (1, 1): up=6, left=8, down=4, right=2 -> val = min = 2
    assert minPath(grid, 3) == [1, 2, 1]
    assert minPath(grid, 4) == [1, 2, 1, 2]
    assert minPath(grid, 1) == [1]


def test_min_path_one_in_top_left_corner():
    """1 at (0, 0): 'i != 0' and 'j != 0' branches are False,
    'i != n-1' and 'j != n-1' branches are True."""
    grid = [
        [1, 2],
        [3, 4],
    ]
    # Neighbours of (0, 0): down=3, right=2 -> val = 2
    assert minPath(grid, 2) == [1, 2]


def test_min_path_one_in_bottom_right_corner():
    """1 at (n-1, n-1): 'i != 0' and 'j != 0' branches are True,
    'i != n-1' and 'j != n-1' branches are False."""
    grid = [
        [2, 3],
        [4, 1],
    ]
    # Neighbours of (1, 1): up=3, left=4 -> val = 3
    assert minPath(grid, 2) == [1, 3]


def test_min_path_one_in_top_right_corner():
    """1 at (0, n-1): covers the remaining (F, T, T, F) branch combination."""
    grid = [
        [2, 1],
        [3, 4],
    ]
    # Neighbours of (0, 1): left=2, down=4 -> val = 2
    assert minPath(grid, 2) == [1, 2]


def test_min_path_one_in_bottom_left_corner():
    """1 at (n-1, 0): covers the remaining (T, F, F, T) branch combination."""
    grid = [
        [2, 3],
        [1, 4],
    ]
    # Neighbours of (1, 0): up=2, right=4 -> val = 2
    assert minPath(grid, 2) == [1, 2]


def test_min_path_without_one_keeps_initial_val():
    """No cell equals 1: the 'grid[i][j] == 1' branch is never taken, so
    val keeps its initial value n*n + 1."""
    grid = [
        [2, 3],
        [4, 5],
    ]
    assert minPath(grid, 2) == [1, 5]
    assert minPath(grid, 3) == [1, 5, 1]


def test_min_path_k_zero_returns_empty_list():
    """k = 0 skips the answer loop entirely and returns an empty list."""
    grid = [
        [1, 2],
        [3, 4],
    ]
    assert minPath(grid, 0) == []
