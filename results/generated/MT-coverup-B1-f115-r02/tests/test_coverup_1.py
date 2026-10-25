# file: project/f115/__init__.py:1-4
# asked: {"lines": [2, 4], "branches": []}
# gained: {"lines": [2, 4], "branches": []}

from f115 import max_fill


def test_max_fill_basic_single_capacity():
    grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
    result = max_fill(grid, 1)
    assert result == 6


def test_max_fill_with_ceiling():
    grid = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
    result = max_fill(grid, 2)
    # row sums are 2, 0, 4, 3 -> ceils are 1, 0, 2, 2
    assert result == 5


def test_max_fill_empty_grid():
    assert max_fill([], 1) == 0


def test_max_fill_all_zeros():
    assert max_fill([[0, 0, 0], [0, 0, 0]], 1) == 0


def test_max_fill_partial_bucket():
    # sum=3, capacity=2 -> ceil(1.5) == 2
    assert max_fill([[1, 1, 1]], 2) == 2
