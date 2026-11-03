# file: project/f068/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}

import pytest

from f068 import pluck


def test_pluck_empty_list_returns_empty():
    """Exercises line 3 (true branch): an empty array short-circuits to []."""
    result = pluck([])
    assert result == []


@pytest.mark.parametrize("arr", [[1, 3, 5, 7], [9], [-1, -3]])
def test_pluck_no_even_values_returns_empty(arr):
    """Exercises lines 3 (false branch), 4 and 5 (true branch):
    a list containing only odd values yields no evens, so []."""
    snapshot = list(arr)  # guard against accidental mutation
    result = pluck(arr)
    assert result == []
    assert arr == snapshot  # input untouched


def test_pluck_returns_smallest_even_and_first_index():
    """Exercises lines 3-6 fully: normal path returns
    [min(evens), index of first occurrence of min(evens)]."""
    result = pluck([5, 0, 3, 0, 4, 2])
    # evens = [0, 0, 4, 2] -> min is 0, first index of 0 is 1
    assert result == [0, 1]


def test_pluck_with_negative_evens():
    """Even negative values count as even in Python (-2 % 2 == 0)."""
    result = pluck([-3, -2, 5, 4])
    # evens = [-2, 4] -> min is -2 at index 1
    assert result == [-2, 1]


def test_pluck_does_not_mutate_input():
    """Postcondition: pluck is non-destructive."""
    arr = [4, 2, 3]
    original = list(arr)
    result = pluck(arr)
    assert result == [2, 1]
    assert arr == original
