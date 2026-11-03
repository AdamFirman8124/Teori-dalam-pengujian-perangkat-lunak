

# Generated at 2026-11-02 20:55:15.904300
# Unit test for function minPath
def test_minPath():
    # 1 at corner, min neighbor is 2
    assert module_0.minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) == [1, 2, 1]

    # k = 1 returns just [1]
    assert module_0.minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [1]

    # 1 in center, min neighbor is 4
    assert module_0.minPath([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 4) == [1, 4, 1, 4]

    # k = 0 returns empty list
    assert module_0.minPath([[1, 2], [3, 4]], 0) == []

    # 1 on edge (not corner), min neighbor is 2
    assert module_0.minPath([[2, 1], [3, 4]], 3) == [1, 2, 1]

    # 1x2 grid, only one neighbor
    assert module_0.minPath([[10, 1]], 2) == [1, 10]

    # odd k, alternating pattern
    assert module_0.minPath([[1, 2], [3, 4]], 5) == [1, 2, 1, 2, 1]

    # 1 in middle of larger grid, min neighbor is 2
    assert module_0.minPath([[9, 9, 9], [9, 1, 2], [9, 3, 9]], 6) == [1, 2, 1, 2, 1, 2]

    print("All minPath tests passed!")


test_minPath()

# Generated at 2026-11-02 20:55:43.305738
# Unit test for function minPath
def test_minPath():
    # 1 at top-left corner: neighbors are right=2, down=4 -> val=2
    assert module_0.minPath([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]], 3) == [1, 2, 1]

    # Same grid, longer path alternates 1 and val
    assert module_0.minPath([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]], 5) == [1, 2, 1, 2, 1]

    # 1 at top-left of 2x2 grid: neighbors right=2, down=3 -> val=2
    assert module_0.minPath([[1, 2],
                    [3, 4]], 4) == [1, 2, 1, 2]

    # 1 at bottom-right corner: neighbors up=6, left=7 -> val=6
    assert module_0.minPath([[5, 6],
                    [7, 1]], 3) == [1, 6, 1]

    # 1 at top-right: neighbors left=2, down=3 -> val=2
    assert module_0.minPath([[2, 1],
                    [4, 3]], 2) == [1, 2]

    # k=1 returns only the starting value
    assert module_0.minPath([[1, 2],
                    [3, 4]], 1) == [1]

    # 1 not at corner, larger neighbor values: left=10, down=12 -> val=10
    assert module_0.minPath([[10, 1],
                    [11, 12]], 4) == [1, 10, 1, 10]

    # 1 in center of 3x3 grid: min neighbor is 2
    assert module_0.minPath([[9, 8, 7],
                    [2, 1, 3],
                    [6, 5, 4]], 3) == [1, 2, 1]

    # 1 in middle of left edge: neighbors up=4, down=8, right=5 -> val=4
    assert module_0.minPath([[3, 2, 9],
                    [4, 1, 5],
                    [8, 7, 6]], 4) == [1, 4, 1, 4]

    # Single-cell grid, k=1
    assert module_0.minPath([[1]], 1) == [1]

    print("All tests passed!")

# Generated at 2026-11-02 20:56:38.611825
# Unit test for function minPath
def test_minPath():
    # 1 at corner (0,0): neighbors are 4 (down) and 2 (right) -> min is 2
    assert module_0.minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) == [1, 2, 1]
    assert module_0.minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [1]
    assert module_0.minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4) == [1, 2, 1, 2]

    # 1 in the middle: neighbors are 9, 4, 8, 6 -> min is 4
    assert module_0.minPath([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1) == [1]
    assert module_0.minPath([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 5) == [1, 4, 1, 4, 1]

    # 1 at top-left of 2x2 grid
    assert module_0.minPath([[1, 3], [2, 4]], 2) == [1, 2]
    assert module_0.minPath([[1, 2], [3, 4]], 6) == [1, 2, 1, 2, 1, 2]

    # 1 at bottom-left corner: neighbors are 4 (up) and 2 (right) -> min is 2
    assert module_0.minPath([[7, 8, 9], [4, 5, 6], [1, 2, 3]], 4) == [1, 2, 1, 2]

    # 1 at bottom-middle: neighbors are 2 (up), 7 (left), 9 (right) -> min is 2
    assert module_0.minPath([[11, 6, 10], [12, 2, 8], [7, 1, 9]], 3) == [1, 2, 1]

    # 1 at top-right corner: neighbors are 4 (down) and 7 (left) -> min is 4
    assert module_0.minPath([[8, 7, 1], [9, 5, 6], [3, 2, 4]], 6) == [1, 4, 1, 4, 1, 4]

test_minPath()

# Generated at 2026-11-02 20:57:44.856874
# Unit test for function minPath
def test_minPath():
    # 1 in top-left corner: neighbors are down (4) and right (2) -> val = 2
    grid1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert module_0.minPath(grid1, 1) == [1]
    assert module_0.minPath(grid1, 3) == [1, 2, 1]
    assert module_0.minPath(grid1, 5) == [1, 2, 1, 2, 1]

    # 1 in the middle: neighbors up(9), left(4), down(8), right(6) -> val = 4
    grid2 = [[5, 9, 3], [4, 1, 6], [7, 8, 2]]
    assert module_0.minPath(grid2, 4) == [1, 4, 1, 4]
    assert module_0.minPath(grid2, 6) == [1, 4, 1, 4, 1, 4]

    # 1 in bottom-left corner: neighbors up(4) and right(2) -> val = 2
    grid3 = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    assert module_0.minPath(grid3, 3) == [1, 2, 1]

    # 1 on top-right of 2x2 grid: neighbors left(2) and down(4) -> val = 2
    grid4 = [[2, 1], [3, 4]]
    assert module_0.minPath(grid4, 3) == [1, 2, 1]

    # 1 in bottom-right of 2x2 grid: neighbors up(2) and left(4) -> val = 2
    grid5 = [[3, 2], [4, 1]]
    assert module_0.minPath(grid5, 5) == [1, 2, 1, 2, 1]

    # 1 in bottom-right of 4x4 grid: neighbors up(12) and left(5) -> val = 5
    grid6 = [[16, 2, 3, 13], [5, 11, 10, 8], [9, 7, 6, 12], [4, 20, 5, 1]]
    assert module_0.minPath(grid6, 4) == [1, 5, 1, 5]

    # 1 in middle of 4x4 grid: neighbors up(30), left(60), down(100), right(70) -> val = 30
    grid7 = [[10, 20, 30, 40], [50, 60, 1, 70], [80, 90, 100, 110], [120, 130, 140, 150]]
    assert module_0.minPath(grid7, 6) == [1, 30, 1, 30, 1, 30]

    # 1 where the right neighbor is the minimum -> val = 2
    grid8 = [[5, 1, 2], [8, 9, 7], [6, 4, 3]]
    assert module_0.minPath(grid8, 4) == [1, 2, 1, 2]

    print("All test cases passed!")


test

# Generated at 2026-11-02 20:59:11.701117
# Unit test for function minPath
def test_minPath():
    # Test case 1: 1 in the corner, k=3
    grid = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    assert module_0.minPath(grid, 3) == [1, 2, 1]

    # Test case 2: 1 in the middle, k=1
    grid = [[5, 9, 3],
            [4, 1, 6],
            [7, 8, 2]]
    assert module_0.minPath(grid, 1) == [1]

    # Test case 3: 1 in the middle, k=4
    grid = [[5, 9, 3],
            [4, 1, 6],
            [7, 8, 2]]
    assert module_0.minPath(grid, 4) == [1, 4, 1, 4]

    # Test case 4: 1 at bottom-right corner, k=5
    grid = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]
    assert module_0.minPath(grid, 5) == [1, 2, 1, 2, 1]

    # Test case 5: 2x2 grid, 1 at top-left, k=2
    grid = [[1, 3],
            [2, 4]]
    assert module_0.minPath(grid, 2) == [1, 2]

    # Test case 6: 1x1 grid (only value 1, no neighbors -> val stays n*n+1)
    grid = [[1]]
    assert module_0.minPath(grid, 3) == [1, 2, 1]  # n*n+1 = 2

    # Test case 7: larger grid, 1 not adjacent to smallest values
    grid = [[10, 20, 30],
            [40, 50, 60],
            [70, 80, 1]]
    assert module_0.minPath(grid, 6) == [1, 60, 1, 60, 1, 60]

    # Test case 8: k=0 returns empty list
    grid = [[1, 2],
            [3, 4]]
    assert module_0.minPath(grid, 0) == []

    print("All test cases passed!")


test_minPath()