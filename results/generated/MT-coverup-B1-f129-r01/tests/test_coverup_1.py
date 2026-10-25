# file: project/f129/__init__.py:1-29
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}

from f129 import minPath


def test_top_left_corner():
    grid = [[1, 2], [3, 4]]
    # neighbors of 1 at (0,0): 3 (down), 2 (right) -> val = 2
    assert minPath(grid, 3) == [1, 2, 1]
    assert grid == [[1, 2], [3, 4]]


def test_bottom_right_corner():
    grid = [[4, 3], [2, 1]]
    # neighbors of 1 at (1,1): 3 (up), 2 (left) -> val = 2
    assert minPath(grid, 4) == [1, 2, 1, 2]
    assert grid == [[4, 3], [2, 1]]


def test_top_right_corner():
    grid = [[2, 3, 1], [4, 5, 6], [7, 8, 9]]
    # neighbors of 1 at (0,2): 3 (left), 6 (down) -> val = 3
    assert minPath(grid, 3) == [1, 3, 1]
    assert grid == [[2, 3, 1], [4, 5, 6], [7, 8, 9]]


def test_bottom_left_corner():
    grid = [[2, 3, 4], [5, 6, 7], [1, 8, 9]]
    # neighbors of 1 at (2,0): 5 (up), 8 (right) -> val = 5
    assert minPath(grid, 2) == [1, 5]
    assert grid == [[2, 3, 4], [5, 6, 7], [1, 8, 9]]


def test_center():
    grid = [[2, 3, 4], [5, 1, 6], [7, 8, 9]]
    # neighbors of 1 at (1,1): 3 (up), 5 (left), 8 (down), 6 (right) -> val = 3
    assert minPath(grid, 5) == [1, 3, 1, 3, 1]
    assert grid == [[2, 3, 4], [5, 1, 6], [7, 8, 9]]


def test_top_edge_middle():
    grid = [[2, 1, 3], [4, 5, 6], [7, 8, 9]]
    # neighbors of 1 at (0,1): 2 (left), 3 (right), 5 (down) -> val = 2
    assert minPath(grid, 2) == [1, 2]
    assert grid == [[2, 1, 3], [4, 5, 6], [7, 8, 9]]


def test_bottom_edge_middle():
    grid = [[2, 3, 4], [5, 6, 7], [8, 1, 9]]
    # neighbors of 1 at (2,1): 6 (up), 8 (left), 9 (right) -> val = 6
    assert minPath(grid, 1) == [1]
    assert grid == [[2, 3, 4], [5, 6, 7], [8, 1, 9]]


def test_left_edge_middle():
    grid = [[2, 3, 4], [1, 5, 6], [7, 8, 9]]
    # neighbors of 1 at (1,0): 2 (up), 7 (down), 5 (right) -> val = 2
    assert minPath(grid, 2) == [1, 2]


def test_right_edge_middle():
    grid = [[2, 3, 4], [5, 6, 1], [7, 8, 9]]
    # neighbors of 1 at (1,2): 4 (up), 9 (down), 6 (left) -> val = 4
    assert minPath(grid, 4) == [1, 4, 1, 4]


def test_k_zero():
    grid = [[1, 2], [3, 4]]
    assert minPath(grid, 0) == []
