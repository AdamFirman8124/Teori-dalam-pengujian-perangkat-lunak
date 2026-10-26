# file: project/f115/__init__.py:1-4
# asked: {"lines": [2, 4], "branches": []}
# gained: {"lines": [2, 4], "branches": []}

from f115 import max_fill


def test_max_fill_calculates_rounded_up_capacity_requirements():
    grid = [[1, 2], [3, 4], [0, 0]]

    assert max_fill(grid, 3) == 4


def test_max_fill_with_empty_grid():
    assert max_fill([], 5) == 0
