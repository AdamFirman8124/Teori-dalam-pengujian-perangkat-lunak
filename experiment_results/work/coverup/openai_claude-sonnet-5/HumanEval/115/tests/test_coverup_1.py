# file: script_115.py:1-36
# asked: {"lines": [2, 3, 36], "branches": []}
# gained: {"lines": [2, 3, 36], "branches": []}

import pytest
from script_115 import max_fill


def test_max_fill_example_1():
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    bucket_capacity = 1
    result = max_fill(grid, bucket_capacity)
    assert result == 6


def test_max_fill_example_2():
    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    bucket_capacity = 2
    result = max_fill(grid, bucket_capacity)
    assert result == 5


def test_max_fill_example_3():
    grid = [[0,0,0], [0,0,0]]
    bucket_capacity = 5
    result = max_fill(grid, bucket_capacity)
    assert result == 0


def test_max_fill_single_well_single_unit():
    grid = [[1]]
    bucket_capacity = 1
    result = max_fill(grid, bucket_capacity)
    assert result == 1


def test_max_fill_single_well_multiple_units():
    grid = [[1,1,1,1,1]]
    bucket_capacity = 2
    result = max_fill(grid, bucket_capacity)
    assert result == 3


def test_max_fill_empty_grid():
    grid = []
    bucket_capacity = 5
    result = max_fill(grid, bucket_capacity)
    assert result == 0


def test_max_fill_large_capacity():
    grid = [[1,1,1], [1,1,1]]
    bucket_capacity = 10
    result = max_fill(grid, bucket_capacity)
    assert result == 2


def test_max_fill_capacity_equals_water():
    grid = [[1,1,1,1]]
    bucket_capacity = 4
    result = max_fill(grid, bucket_capacity)
    assert result == 1
