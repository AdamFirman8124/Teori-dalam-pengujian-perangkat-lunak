# file: project/f129/__init__.py:1-29
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}

from copy import deepcopy

from f129 import minPath


def test_min_path_covers_boundaries_neighbors_and_alternating_result():
    grid = [
        [1, 2, 3],
        [4, 1, 5],
        [6, 7, 1],
    ]
    original_grid = deepcopy(grid)

    assert minPath(grid, 4) == [1, 5, 1, 5]
    assert grid == original_grid
