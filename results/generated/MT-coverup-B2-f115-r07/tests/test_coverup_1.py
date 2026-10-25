# file: project/f115/__init__.py:1-4
# asked: {"lines": [2, 4], "branches": []}
# gained: {"lines": [2, 4], "branches": []}

import pytest

from f115 import max_fill


def test_max_fill_single_row_exact_division():
    # sum(arr) = 6, capacity = 3 -> ceil(6/3) = 2
    assert max_fill([[1, 1, 1, 1, 1, 1]], 3) == 2


def test_max_fill_multiple_rows_with_remainder():
    # ceil(5/4) = 2, ceil(4/4) = 1, ceil(7/4) = 2 -> total 5
    grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]
    assert max_fill(grid, 4) == 5


def test_max_fill_empty_grid():
    assert max_fill([], 5) == 0


def test_max_fill_empty_rows():
    # sum([]) = 0, ceil(0/capacity) = 0 for each row
    assert max_fill([[], [], []], 2) == 0


def test_max_fill_capacity_larger_than_row_sum():
    # ceil(3/10) = 1
    assert max_fill([[1, 1, 1]], 10) == 1
