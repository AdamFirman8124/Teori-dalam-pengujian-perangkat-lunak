# file: project/f129/__init__.py:1-29
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 25, 26, 28, 29], "branches": [[5, 6], [5, 23], [6, 5], [6, 7], [7, 6], [7, 8], [9, 10], [9, 12], [12, 13], [12, 15], [15, 16], [15, 18], [18, 19], [18, 21], [24, 25], [24, 29], [25, 26], [25, 28]]}

from f129 import minPath


def test_top_left_corner():
    grid = [[1, 2], [3, 4]]
    # (0,0): i==0, j==0, neighbors 3 and 2 -> val 2
    assert minPath(grid, 4) == [1, 2, 1, 2]


def test_top_right_corner():
    grid = [[2, 1], [3, 4]]
    # (0,1): i==0 False-branch, j!=0 True, i!=n-1 True, j==n-1 False-branch
    # neighbors: grid[0][0]=2, grid[1][1]=4 -> val 2
    assert minPath(grid, 3) == [1, 2, 1]


def test_bottom_left_corner():
    grid = [[2, 3], [1, 4]]
    # (1,0): i!=0 True, j==0 False-branch, i==n-1 False-branch, j!=n-1 True
    # neighbors: grid[0][0]=2, grid[1][1]=4 -> val 2
    assert minPath(grid, 2) == [1, 2]


def test_bottom_right_corner():
    grid = [[4, 3], [2, 1]]
    # (1,1): i!=0 True, j!=0 True, i==n-1 False-branch, j==n-1 False-branch
    # neighbors: grid[0][1]=3, grid[1][0]=2 -> val 2
    assert minPath(grid, 5) == [1, 2, 1, 2, 1]


def test_center_all_neighbors():
    grid = [[2, 3, 4], [5, 1, 6], [7, 8, 9]]
    # (1,1): all four neighbor branches True -> [3,5,8,6] -> val 3
    assert minPath(grid, 4) == [1, 3, 1, 3]


def test_top_edge():
    grid = [[4, 1, 5], [6, 7, 8], [9, 10, 11]]
    # (0,1): i==0, j!=0, i!=n-1, j!=n-1 -> [4,7,5] -> val 4
    assert minPath(grid, 2) == [1, 4]


def test_bottom_edge():
    grid = [[4, 5, 6], [7, 8, 9], [10, 1, 11]]
    # (2,1): i!=0 True, j!=0 True, i==n-1 False, j!=n-1 True -> [8,10,11] -> val 8
    assert minPath(grid, 3) == [1, 8, 1]


def test_left_edge():
    grid = [[4, 5, 6], [1, 8, 9], [10, 11, 12]]
    # (1,0): i!=0 True, j==0 False, i!=n-1 True, j!=n-1 True -> [4,10,8] -> val 4
    assert minPath(grid, 2) == [1, 4]


def test_right_edge():
    grid = [[4, 5, 6], [7, 8, 1], [10, 11, 12]]
    # (1,2): i!=0 True, j!=0 True, i!=n-1 True, j==n-1 False -> [6,8,12] -> val 6
    assert minPath(grid, 2) == [1, 6]


def test_k_zero_and_one():
    grid = [[1, 2], [3, 4]]
    # k=0: second loop zero iterations, covers loop-exit branch
    assert minPath(grid, 0) == []
    # k=1: only i%2==0 True-branch
    assert minPath(grid, 1) == [1]
    # k=2: covers both i%2==0 True and False branches
    assert minPath(grid, 2) == [1, 2]
