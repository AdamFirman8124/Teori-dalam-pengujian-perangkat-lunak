# file: project/f129/__init__.py:1-29
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [18, 19], [24, 25], [24, 29], [25, 26], [25, 28]]}

import pytest

from f129 import minPath


def test_min_path_interior_one_covers_all_neighbour_branches():
    """1 sits in the interior of a 3x3 grid, so the 'i != 0' and 'j != 0'
    branches are taken (True) while 'i != n - 1' and 'j != n - 1' are not
    (False).  Neighbours of 1 are 3 (up), 5 (left), 6 (right), 8 (down),
    so val = 3.  Both the even and odd branches of the k-loop run."""
    grid = [
        [2, 3, 4],
        [5, 1, 6],
        [7, 8, 9],
    ]
    assert minPath(grid, 4) == [1, 3, 1, 3]


def test_min_path_corner_one_covers_remaining_neighbour_branches():
    """1 sits in the top-left corner of a 2x2 grid, so 'i != 0' and
    'j != 0' are False while 'i != n - 1' and 'j != n - 1' are True.
    Neighbours of 1 are 3 (down) and 2 (right), so val = 2."""
    grid = [
        [1, 2],
        [3, 4],
    ]
    assert minPath(grid, 2) == [1, 2]


def test_min_path_no_one_in_grid_uses_initial_val():
    """No cell equals 1, so the inner 'if grid[i][j] == 1' branch is never
    taken and val keeps its initial value n * n + 1 = 5, which is used at
    odd positions of the answer."""
    grid = [
        [2, 4],
        [6, 8],
    ]
    assert minPath(grid, 3) == [1, 5, 1]


def test_min_path_zero_length_returns_empty_list():
    """k = 0 produces an empty path; the k-loop body (and its even/odd
    branches) is skipped entirely."""
    grid = [
        [1, 2],
        [3, 4],
    ]
    assert minPath(grid, 0) == []
