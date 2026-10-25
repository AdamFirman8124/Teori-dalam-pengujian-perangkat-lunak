# file: project/f115/__init__.py:1-4
# asked: {"lines": [2, 4], "branches": []}
# gained: {"lines": [2, 4], "branches": []}

import pytest

from f115 import max_fill


def test_max_fill_empty_grid():
    assert max_fill([], 1) == 0


def test_max_fill_all_zero_rows():
    assert max_fill([[0, 0], [0, 0, 0]], 5) == 0


def test_max_fill_single_row_exact_capacity():
    assert max_fill([[1, 1, 1]], 3) == 1


def test_max_fill_single_row_needs_rounding_up():
    assert max_fill([[1, 1, 1, 1]], 3) == 2


def test_max_fill_multiple_rows():
    grid = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]]
    assert max_fill(grid, 1) == 6
    assert max_fill(grid, 2) == 4
    assert max_fill(grid, 3) == 4


def test_max_fill_does_not_mutate_input():
    grid = [[1, 0, 1], [0, 1, 0]]
    snapshot = [row[:] for row in grid]
    max_fill(grid, 2)
    assert grid == snapshot


def test_max_fill_returns_int():
    result = max_fill([[1, 1], [1, 1]], 2)
    assert isinstance(result, int)
    assert result == 2


def test_max_fill_imports_math_lazily(monkeypatch):
    import math

    calls = []
    real_ceil = math.ceil

    def spy_ceil(value):
        calls.append(value)
        return real_ceil(value)

    monkeypatch.setattr(math, "ceil", spy_ceil)
    assert max_fill([[1, 1, 1]], 2) == 2
    assert calls == [1.5]
