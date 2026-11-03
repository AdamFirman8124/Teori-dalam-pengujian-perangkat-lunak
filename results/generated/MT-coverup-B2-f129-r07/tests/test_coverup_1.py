# file: project/f129/__init__.py:1-29
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}

"""Tests for f129.minPath covering all previously unexecuted lines (3-29)
and every branch of the neighbor checks and the parity check.

minPath is a pure function (no I/O, no module state), so local grid data
is used and no monkeypatching/cleanup is required to avoid state pollution.
"""

from f129 import minPath


def test_min_path_center_all_neighbor_branches_true():
    """1 in the middle of a 3x3 grid: i!=0, j!=0, i!=n-1 and j!=n-1 all True."""
    grid = [
        [3, 2, 4],
        [5, 1, 6],
        [7, 8, 9],
    ]
    # neighbors of (1,1): up=2, left=5, down=8, right=6 -> val = 2
    assert minPath(grid, 4) == [1, 2, 1, 2]
    # odd k ends on the else-branch value
    assert minPath(grid, 5) == [1, 2, 1, 2, 1]


def test_min_path_top_left_corner():
    """1 at (0, 0): i!=0 and j!=0 are False; i!=n-1 and j!=n-1 are True."""
    grid = [
        [1, 5, 9],
        [4, 3, 8],
        [7, 6, 2],
    ]
    # neighbors of (0,0): down=4, right=5 -> val = 4
    assert minPath(grid, 4) == [1, 4, 1, 4]


def test_min_path_bottom_right_corner():
    """1 at (n-1, n-1): i!=n-1 and j!=n-1 are False; i!=0 and j!=0 are True."""
    grid = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ]
    # neighbors of (2,2): up=5, left=2 -> val = 2
    assert minPath(grid, 3) == [1, 2, 1]


def test_min_path_top_right_corner():
    """1 at (0, n-1): i!=0 and j!=n-1 are False; j!=0 and i!=n-1 are True."""
    grid = [
        [9, 8, 1],
        [6, 5, 4],
        [3, 2, 7],
    ]
    # neighbors of (0,2): left=8, down=4 -> val = 4
    assert minPath(grid, 2) == [1, 4]


def test_min_path_bottom_left_corner():
    """1 at (n-1, 0): i!=n-1 and j!=0 are False; i!=0 and j!=n-1 are True."""
    grid = [
        [9, 8, 7],
        [6, 5, 4],
        [1, 2, 3],
    ]
    # neighbors of (2,0): up=5, right=2 -> val = 2
    assert minPath(grid, 5) == [1, 2, 1, 2, 1]


def test_min_path_top_edge():
    """1 at (0, 1): i!=0 False; j!=0, i!=n-1, j!=n-1 True."""
    grid = [
        [2, 1, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    # neighbors of (0,1): left=2, down=5, right=3 -> val = 2
    assert minPath(grid, 3) == [1, 2, 1]


def test_min_path_left_edge():
    """1 at (1, 0): j!=0 False; i!=0, i!=n-1, j!=n-1 True."""
    grid = [
        [2, 3, 4],
        [1, 5, 6],
        [7, 8, 9],
    ]
    # neighbors of (1,0): up=2, down=7, right=5 -> val = 2
    assert minPath(grid, 2) == [1, 2]


def test_min_path_right_edge():
    """1 at (1, n-1): j!=n-1 False; i!=0, j!=0, i!=n-1 True."""
    grid = [
        [2, 3, 4],
        [5, 6, 1],
        [7, 8, 9],
    ]
    # neighbors of (1,2): up=4, left=6, down=9 -> val = 4
    assert minPath(grid, 4) == [1, 4, 1, 4]


def test_min_path_bottom_edge():
    """1 at (n-1, 1): i!=n-1 False; i!=0, j!=0, j!=n-1 True."""
    grid = [
        [2, 3, 4],
        [5, 6, 7],
        [8, 1, 9],
    ]
    # neighbors of (2,1): up=6, left=8, right=9 -> val = 6
    assert minPath(grid, 3) == [1, 6, 1]


def test_min_path_no_one_uses_default_val():
    """No cell equals 1: the inner if is never True and val stays n*n + 1."""
    grid = [
        [2, 3],
        [4, 5],
    ]
    assert minPath(grid, 2) == [1, 5]
    assert minPath(grid, 3) == [1, 5, 1]


def test_min_path_k_zero_returns_empty_list():
    """k == 0: the answer loop body never runs and an empty list is returned."""
    grid = [
        [2, 3],
        [4, 1],
    ]
    assert minPath(grid, 0) == []
