# file: project/f115/__init__.py:1-4
# asked: {"lines": [2, 4], "branches": []}
# gained: {"lines": [2, 4], "branches": []}

import math

import pytest

from f115 import max_fill


def test_max_fill_single_trip_per_well():
    """Each well needs at most one bucket trip (capacity >= row sum)."""
    grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
    capacity = 1
    # sums: 1, 1, 4 -> ceil(1/1) + ceil(1/1) + ceil(4/1) = 6
    assert max_fill(grid, capacity) == 6


def test_max_fill_multiple_trips_per_well():
    """Wells whose sum exceeds capacity require multiple trips (ceil behavior)."""
    grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
    capacity = 2
    # sums: 2, 0, 4, 3 -> ceil(2/2) + ceil(0/2) + ceil(4/2) + ceil(3/2) = 1 + 0 + 2 + 2
    assert max_fill(grid, capacity) == 5


def test_max_fill_empty_grid():
    """An empty grid requires no trips."""
    assert max_fill([], 5) == 0


def test_max_fill_empty_rows():
    """Rows with no water contribute zero trips."""
    grid = [[], [0, 0], []]
    assert max_fill(grid, 3) == 0


def test_max_fill_capacity_larger_than_any_well():
    """A large capacity still yields one trip per non-empty well."""
    grid = [[1, 1, 1], [1]]
    assert max_fill(grid, 10) == 2


def test_max_fill_matches_reference_implementation():
    """Cross-check against an independent reference computation."""
    grid = [[3, 2, 6], [1, 1, 1, 1], [7], [0]]
    capacity = 5
    expected = sum(math.ceil(sum(row) / capacity) for row in grid)
    assert max_fill(grid, capacity) == expected
    # ceil(11/5)=3, ceil(4/5)=1, ceil(7/5)=2, ceil(0/5)=0 -> 6
    assert expected == 6
