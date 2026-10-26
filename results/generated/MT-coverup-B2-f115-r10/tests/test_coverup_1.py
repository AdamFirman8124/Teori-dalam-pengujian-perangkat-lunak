# file: project/f115/__init__.py:1-4
# asked: {"lines": [2, 4], "branches": []}
# gained: {"lines": [2, 4], "branches": []}

from f115 import max_fill


def test_max_fill_rounds_each_row_up():
    grid = [[1, 2, 3], [4, 5], [], [10]]
    original = [row.copy() for row in grid]

    assert max_fill(grid, 4) == 8
    assert grid == original


def test_max_fill_empty_grid():
    assert max_fill([], 5) == 0
