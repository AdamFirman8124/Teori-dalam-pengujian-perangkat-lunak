# file: project/f129/__init__.py:1-29
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}

"""Tests for f129.minPath, covering all previously unexecuted lines 3-29
and every branch therein.

minPath is a pure function (no I/O, no module state, no globals), so no
monkeypatching or teardown is required; each test builds its own local
grid, guaranteeing no state pollution between tests.
"""

from f129 import minPath


def test_min_path_center_hits_all_neighbor_branches():
    # '1' at the center of a 3x3 grid: all four neighbor conditions
    # (i != 0, j != 0, i != n-1, j != n-1) are True -> lines 9-21 all run.
    grid = [
        [5, 2, 6],
        [3, 1, 4],
        [8, 7, 9],
    ]
    # Neighbors of (1, 1): up=2, left=3, down=7, right=4 -> val = min = 2
    assert minPath(grid, 4) == [1, 2, 1, 2]
    # Odd k exercises both the even (line 26) and odd (line 28) branches.
    assert minPath(grid, 5) == [1, 2, 1, 2, 1]


def test_min_path_top_left_corner():
    # '1' at (0, 0): 'i != 0' and 'j != 0' are False; the other two are True.
    grid = [
        [1, 2],
        [3, 4],
    ]
    # Neighbors: down=3, right=2 -> val = 2
    assert minPath(grid, 3) == [1, 2, 1]


def test_min_path_bottom_right_corner():
    # '1' at (n-1, n-1): 'i != n-1' and 'j != n-1' are False.
    grid = [
        [2, 3],
        [4, 1],
    ]
    # Neighbors: up=3, left=4 -> val = 3
    assert minPath(grid, 2) == [1, 3]


def test_min_path_top_right_corner():
    # '1' at (0, n-1): 'i != 0' and 'j != n-1' are False.
    grid = [
        [2, 1],
        [3, 4],
    ]
    # Neighbors: left=2, down=4 -> val = 2
    assert minPath(grid, 2) == [1, 2]


def test_min_path_bottom_left_corner():
    # '1' at (n-1, 0): 'j != 0' and 'i != n-1' are False.
    grid = [
        [2, 3],
        [1, 4],
    ]
    # Neighbors: up=2, right=4 -> val = 2
    assert minPath(grid, 2) == [1, 2]


def test_min_path_without_one_uses_default_val():
    # No cell equals 1: the False branch of 'if grid[i][j] == 1' is taken
    # and val keeps its initial value n*n + 1 (line 4).
    grid = [
        [2, 3],
        [4, 5],
    ]
    assert minPath(grid, 3) == [1, 5, 1]


def test_min_path_k_zero_returns_empty_list():
    # k == 0: the answer loop body never runs; an empty list is returned.
    grid = [
        [1, 2],
        [3, 4],
    ]
    assert minPath(grid, 0) == []
