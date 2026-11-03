# file: project/f115/__init__.py:1-4
# asked: {"lines": [2, 4], "branches": []}
# gained: {"lines": [2, 4], "branches": []}

import pytest

from f115 import max_fill


def test_max_fill_empty_grid():
    # An empty grid requires no bucket trips; exercises the list comprehension
    # over an empty iterable (sum of nothing == 0).
    assert max_fill([], 1) == 0


def test_max_fill_no_water():
    # Rows containing only zeros: ceil(0/capacity) == 0 for each row.
    assert max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0


def test_max_fill_capacity_one():
    # Classic example: each unit of water needs one trip.
    # Row sums: 1, 1, 4 -> ceil(1/1)+ceil(1/1)+ceil(4/1) == 6.
    assert max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6


def test_max_fill_capacity_two():
    # Row sums: 2, 0, 4, 3 -> ceil(2/2)+ceil(0/2)+ceil(4/2)+ceil(3/2) == 1+0+2+2 == 5.
    assert max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5


def test_max_fill_exact_division():
    # Row sums: 4, 4 with capacity 4 -> 1 + 1 == 2 (no rounding up needed).
    assert max_fill([[1, 1, 1, 1], [1, 1, 1, 1]], 4) == 2


def test_max_fill_partial_bucket():
    # Row sums: 4, 4 with capacity 3 -> ceil(4/3)+ceil(4/3) == 2 + 2 == 4.
    assert max_fill([[1, 1, 1, 1], [1, 1, 1, 1]], 3) == 2 + 2


def test_max_fill_returns_int():
    # math.ceil returns an int, so the result must be an int, not a float.
    result = max_fill([[1, 1, 1]], 2)
    assert isinstance(result, int)
    assert result == 2
