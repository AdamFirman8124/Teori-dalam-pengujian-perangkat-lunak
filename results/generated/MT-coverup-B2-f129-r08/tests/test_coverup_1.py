# file: project/f129/__init__.py:1-29
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}

"""Tests for f129.minPath covering lines 3-29 and all branches.

minPath is a pure function (it does not mutate its arguments, the module, or
any global state), so no monkeypatching or teardown is required to avoid
state pollution.
"""

from f129 import minPath


def test_min_path_center_cell_uses_all_four_neighbors():
    """1 in the middle of a 3x3 grid: all four neighbor branches are True."""
    grid = [
        [2, 3, 4],
        [5, 1, 6],
        [7, 8, 9],
    ]
    # Neighbours of (1, 1): up=3, left=5, down=8, right=6 -> min is 3.
    assert minPath(grid, 4) == [1, 3, 1, 3]


def test_min_path_top_left_corner_skips_up_and_left():
    """1 at (0, 0): 'i != 0' and 'j != 0' branches are False."""
    grid = [
        [1, 2],
        [3, 4],
    ]
    # Neighbours of (0, 0): down=3, right=2 -> min is 2.
    assert minPath(grid, 2) == [1, 2]


def test_min_path_bottom_right_corner_skips_down_and_right():
    """1 at (n-1, n-1): 'i != n-1' and 'j != n-1' branches are False."""
    grid = [
        [2, 3],
        [4, 1],
    ]
    # Neighbours of (1, 1): up=3, left=4 -> min is 3.
    assert minPath(grid, 3) == [1, 3, 1]


def test_min_path_top_right_corner_skips_up_and_right():
    """1 at (0, n-1): 'i != 0' and 'j != n-1' branches are False."""
    grid = [
        [2, 1],
        [3, 4],
    ]
    # Neighbours of (0, 1): left=2, down=4 -> min is 2.
    assert minPath(grid, 2) == [1, 2]


def test_min_path_bottom_left_corner_skips_down_and_left():
    """1 at (n-1, 0): 'j != 0' and 'i != n-1' branches are False."""
    grid = [
        [2, 3],
        [1, 4],
    ]
    # Neighbours of (1, 0): up=2, right=4 -> min is 2.
    assert minPath(grid, 2) == [1, 2]


def test_min_path_without_one_uses_default_val():
    """No 1 anywhere in the grid: 'grid[i][j] == 1' is always False and
    val keeps its initial value n*n + 1."""
    grid = [
        [2, 3],
        [4, 5],
    ]
    # val = 2*2 + 1 = 5.
    assert minPath(grid, 3) == [1, 5, 1]


def test_min_path_k_zero_returns_empty_list():
    """k = 0: the answer loop never runs and an empty list is returned."""
    grid = [
        [1, 2],
        [3, 4],
    ]
    assert minPath(grid, 0) == []


def test_min_path_k_one_only_even_branch():
    """k = 1: only the even branch of 'i % 2 == 0' is exercised."""
    grid = [
        [1, 2],
        [3, 4],
    ]
    assert minPath(grid, 1) == [1]


def test_min_path_does_not_mutate_input():
    """Postcondition: the input grid is left untouched."""
    grid = [
        [2, 3],
        [1, 4],
    ]
    snapshot = [row[:] for row in grid]
    minPath(grid, 3)
    assert grid == snapshot
