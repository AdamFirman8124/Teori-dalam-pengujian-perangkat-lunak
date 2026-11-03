# file: project/f115/__init__.py:1-4
# asked: {"lines": [2, 4], "branches": []}
# gained: {"lines": [2, 4], "branches": []}

import pytest

from f115 import max_fill


def test_max_fill_executes_all_lines():
    # Each row's water units divided by capacity, rounded up, then summed.
    # Row [1, 3] -> sum 4, capacity 5 -> ceil(4/5) = 1
    # Row [2, 2] -> sum 4, capacity 5 -> ceil(4/5) = 1
    # Row [0, 0] -> sum 0, capacity 5 -> ceil(0/5) = 0
    grid = [[1, 3], [2, 2], [0, 0]]
    assert max_fill(grid, 5) == 2


def test_max_fill_exact_division():
    # Exact division should not round up.
    # Row [2, 2] -> sum 4, capacity 2 -> ceil(4/2) = 2
    # Row [1, 1] -> sum 2, capacity 2 -> ceil(2/2) = 1
    assert max_fill([[2, 2], [1, 1]], 2) == 3


def test_max_fill_empty_grid():
    # An empty grid yields zero trips; still exercises lines 2-4.
    assert max_fill([], 3) == 0


def test_max_fill_single_unit_capacity():
    # Capacity 1 means every unit of water needs its own trip.
    # Row [1, 1, 1] -> ceil(3/1) = 3
    # Row [0, 2]    -> ceil(2/1) = 2
    assert max_fill([[1, 1, 1], [0, 2]], 1) == 5
