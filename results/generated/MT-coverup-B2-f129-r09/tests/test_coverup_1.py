# file: project/f129/__init__.py:1-29
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}

import copy

from f129 import minPath


def test_min_path_center_cell_all_four_neighbors():
    """1 in the middle: all four '!=' branches are True, val = min of neighbors."""
    grid = [[2, 2, 2],
            [2, 1, 2],
            [2, 2, 2]]
    snapshot = copy.deepcopy(grid)
    result = minPath(grid, 3)
    # neighbors of the 1 are all 2, so path alternates 1, 2, 1
    assert result == [1, 2, 1]
    assert grid == snapshot  # input grid is not mutated


def test_min_path_top_left_corner():
    """1 at (0, 0): 'i != 0' and 'j != 0' branches are False."""
    grid = [[1, 2],
            [2, 3]]
    snapshot = copy.deepcopy(grid)
    result = minPath(grid, 4)
    # only bottom (2) and right (2) neighbors collected -> val = 2
    assert result == [1, 2, 1, 2]
    assert grid == snapshot


def test_min_path_bottom_right_corner():
    """1 at (n-1, n-1): 'i != n-1' and 'j != n-1' branches are False."""
    grid = [[2, 3],
            [3, 1]]
    snapshot = copy.deepcopy(grid)
    result = minPath(grid, 2)
    # only top (3) and left (3) neighbors collected -> val = 3
    assert result == [1, 3]
    assert grid == snapshot


def test_min_path_without_one_uses_default_val():
    """No cell equals 1: the 'grid[i][j] == 1' branch is never taken,
    so val keeps its initial value n*n + 1."""
    grid = [[2, 3],
            [4, 5]]
    snapshot = copy.deepcopy(grid)
    result = minPath(grid, 3)
    assert result == [1, 5, 1]
    assert grid == snapshot


def test_min_path_alternates_one_and_val():
    """k larger than 2 exercises both parity branches repeatedly."""
    grid = [[1, 4],
            [4, 4]]
    result = minPath(grid, 5)
    assert result == [1, 4, 1, 4, 1]
