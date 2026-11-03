# file: project/f115/__init__.py:1-4
# asked: {"lines": [2, 4], "branches": []}
# gained: {"lines": [2, 4], "branches": []}

import math

import pytest

from f115 import max_fill


def test_max_fill_single_unit_capacity():
    """Each unit of water requires one trip when capacity is 1."""
    grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
    capacity = 1
    # rows need 1, 1 and 4 trips respectively
    assert max_fill(grid, capacity) == 6


def test_max_fill_multiple_units_per_trip():
    """Rows whose water fits in fewer trips are counted with ceiling division."""
    grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
    capacity = 2
    # rows need ceil(2/2)=1, ceil(0/2)=0, ceil(4/2)=2, ceil(3/2)=2 trips
    assert max_fill(grid, capacity) == 5


def test_max_fill_empty_grid():
    """An empty grid requires no trips at all."""
    assert max_fill([], 5) == 0


def test_max_fill_rows_without_water():
    """Rows containing no water contribute zero trips."""
    grid = [[], [0, 0, 0], []]
    assert max_fill(grid, 3) == 0


def test_max_fill_uses_ceil_not_floor():
    """A partial trip must still be counted (ceiling behaviour)."""
    grid = [[1, 1, 1]]
    capacity = 2
    # ceil(3/2) == 2, not floor(3/2) == 1
    assert max_fill(grid, capacity) == math.ceil(3 / 2) == 2
