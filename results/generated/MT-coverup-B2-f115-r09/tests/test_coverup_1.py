# file: project/f115/__init__.py:1-4
# asked: {"lines": [2, 4], "branches": []}
# gained: {"lines": [2, 4], "branches": []}

import math

import pytest

from f115 import max_fill


def test_max_fill_basic_counts_trips_per_row():
    """Each row's total units divided by capacity, rounded up, summed over rows."""
    grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
    # row sums: 1, 1, 4 -> ceil(1/1) + ceil(1/1) + ceil(4/1) = 1 + 1 + 4
    assert max_fill(grid, 1) == 6


def test_max_fill_rounds_up_partial_capacity():
    """Fractional trips must be rounded up (verifies math.ceil is used)."""
    grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
    # row sums: 2, 0, 4, 3 -> ceil(2/2) + ceil(0/2) + ceil(4/2) + ceil(3/2)
    #                        = 1 + 0 + 2 + 2 = 5
    assert max_fill(grid, 2) == 5


def test_max_fill_single_row_fractional():
    """A row whose sum is not a multiple of capacity needs an extra trip."""
    assert max_fill([[1, 1, 1]], 2) == 2  # ceil(3/2) == 2, not 1


def test_max_fill_capacity_larger_than_row_sum():
    """One trip suffices when capacity exceeds the row's total."""
    assert max_fill([[1, 1, 1, 1]], 9) == 1  # ceil(4/9) == 1


def test_max_fill_empty_grid():
    """No rows means no trips are needed."""
    assert max_fill([], 5) == 0


def test_max_fill_empty_row_contributes_zero():
    """An empty row yields ceil(0/capacity) == 0 trips."""
    assert max_fill([[], [1, 1], []], 2) == 1  # 0 + 1 + 0


def test_max_fill_does_not_mutate_input():
    """The function is pure: the grid must be unchanged after the call."""
    grid = [[1, 0], [0, 1]]
    original = [row[:] for row in grid]
    result = max_fill(grid, 1)
    assert result == 2
    assert grid == original
