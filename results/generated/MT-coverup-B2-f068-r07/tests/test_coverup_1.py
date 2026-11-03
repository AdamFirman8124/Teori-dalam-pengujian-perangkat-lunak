# file: project/f068/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}

from f068 import pluck


def test_pluck_empty_array():
    """Covers line 3 (True branch): empty input returns an empty list."""
    assert pluck([]) == []


def test_pluck_no_even_values():
    """Covers lines 3 (False branch), 4 and 5 (True branch):
    an array with only odd values yields no evens, so return []."""
    assert pluck([1, 3, 5, 7]) == []


def test_pluck_single_even_value():
    """Covers lines 3 and 5 (False branches) and line 6:
    a single even value returns the value and its index."""
    assert pluck([3, 2, 5]) == [2, 1]


def test_pluck_returns_smallest_even_and_first_index():
    """Covers line 6: smallest even value with the index of its
    first occurrence (duplicates must resolve to the first index)."""
    assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]


def test_pluck_negative_even_values():
    """Covers line 6 with negative even values: min works on negatives."""
    assert pluck([-2, -4, 3]) == [-4, 1]


def test_pluck_does_not_mutate_input():
    """Postcondition: pluck must not modify the input array."""
    arr = [4, 2, 3]
    snapshot = list(arr)
    pluck(arr)
    assert arr == snapshot
