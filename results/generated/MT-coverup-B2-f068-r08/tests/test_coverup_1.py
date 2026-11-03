# file: project/f068/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}

import pytest

from f068 import pluck


def test_pluck_empty_list():
    """Covers line 3: empty input returns []."""
    assert pluck([]) == []


def test_pluck_no_even_numbers():
    """Covers lines 4-5: all-odd input yields no evens, returns []."""
    assert pluck([1, 3, 5, 7]) == []


def test_pluck_single_even():
    """Covers line 6: single even element returns value and its index."""
    assert pluck([3]) == []
    assert pluck([2]) == [2, 0]


def test_pluck_returns_min_even_and_index():
    """Covers line 6: minimum even value and its index in the original array."""
    assert pluck([5, 4, 3, 2, 1]) == [2, 3]


def test_pluck_min_even_tie_returns_first_index():
    """Covers line 6: duplicate minimum evens resolve to the first occurrence."""
    assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]


def test_pluck_negative_evens():
    """Covers line 6: negative even values are handled correctly."""
    assert pluck([-2, 3, -4, 6]) == [-4, 2]


def test_pluck_does_not_mutate_input():
    """Line 6 must not modify the input list."""
    arr = [4, 2, 3]
    snapshot = list(arr)
    result = pluck(arr)
    assert result == [2, 1]
    assert arr == snapshot
