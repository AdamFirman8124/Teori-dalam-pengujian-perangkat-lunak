# file: project/f115/__init__.py:1-4
# asked: {"lines": [2, 4], "branches": []}
# gained: {"lines": [2, 4], "branches": []}

import pytest

from f115 import max_fill


def test_max_fill_unit_capacity():
    # Each unit of water requires one trip when capacity is 1.
    grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
    assert max_fill(grid, 1) == 6  # 1 + 1 + 4


def test_max_fill_larger_capacity():
    # ceil(2/2) + ceil(0/2) + ceil(4/2) + ceil(3/2) = 1 + 0 + 2 + 2
    grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
    assert max_fill(grid, 2) == 5


def test_max_fill_empty_wells():
    # Wells with no water require no trips.
    assert max_fill([[0, 0], [0, 0]], 5) == 0


def test_max_fill_no_wells():
    # An empty grid yields zero trips.
    assert max_fill([], 3) == 0


def test_max_fill_capacity_divides_exactly():
    # When capacity divides the row sum evenly, no rounding up occurs.
    grid = [[1, 1, 1, 1], [1, 1]]
    assert max_fill(grid, 2) == 3  # ceil(4/2) + ceil(2/2) = 2 + 1
