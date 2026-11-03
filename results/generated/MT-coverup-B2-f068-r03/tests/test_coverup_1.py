# file: project/f068/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}

import pytest

from f068 import pluck


def test_pluck_empty_array():
    """Covers line 3 (len(arr) == 0 branch taken)."""
    assert pluck([]) == []


@pytest.mark.parametrize(
    "arr",
    [
        [1, 3, 5],          # only odd positives
        [-3, -1, 7],        # only odd negatives/mixed
        [1],                # single odd element
    ],
)
def test_pluck_no_evens_returns_empty(arr):
    """Covers lines 3 (branch not taken), 4, and 5 (evens == [] branch taken)."""
    result = pluck(arr)
    assert result == []
    # Postcondition: every element was odd, so filtering yields nothing.
    assert all(x % 2 != 0 for x in arr)


def test_pluck_zero_is_even():
    """Zero counts as even; single-element array with 0 hits line 6."""
    assert pluck([0]) == [0, 0]


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([4, 2, 6], [2, 1]),        # min even not at index 0
        ([2, 4, 6], [2, 0]),        # min even at index 0
        ([1, 2, 3, 4], [2, 1]),     # mixed odd/even
        ([-2, -4, 3], [-4, 1]),     # negative evens
        ([5, 10, 3, 10], [10, 1]),  # duplicate minimum even -> first index
    ],
)
def test_pluck_with_evens(arr, expected):
    """Covers lines 3 (branch not taken), 4, 5 (branch not taken), and 6."""
    result = pluck(arr)
    assert result == expected
    # Postconditions: value is the smallest even number, index points to it.
    evens = [x for x in arr if x % 2 == 0]
    assert result[0] == min(evens)
    assert arr[result[1]] == result[0]
