# file: project/f068/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}

import pytest

from f068 import pluck


def test_pluck_empty_array():
    """Covers line 3 (len(arr) == 0) branch."""
    assert pluck([]) == []


def test_pluck_no_even_numbers():
    """Covers line 5 (evens == []) branch."""
    assert pluck([1, 3, 5, 7]) == []


def test_pluck_returns_min_even_and_index():
    """Covers line 6: returns [min(evens), index of min(evens)]."""
    assert pluck([4, 2, 3]) == [2, 1]


def test_pluck_min_even_takes_first_occurrence():
    """Covers line 6 with duplicate minimum evens: index of first occurrence."""
    assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]


def test_pluck_negative_evens():
    """Covers line 6 with negative even values."""
    assert pluck([-2, -4, 6]) == [-4, 1]


def test_pluck_does_not_mutate_input():
    """Ensures pluck is side-effect free on its argument."""
    arr = [3, 6, 1, 8]
    snapshot = list(arr)
    result = pluck(arr)
    assert arr == snapshot
    assert result == [6, 1]
