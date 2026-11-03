# file: project/f120/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}

import pytest

from f120 import maximum


def test_maximum_k_zero_returns_empty_list():
    """Covers lines 3-4: the k == 0 early-return branch."""
    arr = [3, 1, 2]
    result = maximum(arr, 0)
    assert result == []
    # The early return happens before sorting, so arr must be untouched.
    assert arr == [3, 1, 2]


def test_maximum_k_positive_returns_k_largest_sorted():
    """Covers lines 5-7: sorting and slicing branch."""
    arr = [5, 1, 9, 3, 7]
    result = maximum(arr, 3)
    assert result == [5, 7, 9]
    # arr.sort() mutates the input list in place.
    assert arr == [1, 3, 5, 7, 9]


def test_maximum_k_equals_len_returns_all_sorted():
    """Covers lines 5-7 with k equal to the array length."""
    arr = [2, 8, 4]
    result = maximum(arr, 3)
    assert result == [2, 4, 8]
    assert arr == [2, 4, 8]


def test_maximum_does_not_pollute_caller_state():
    """Ensures the function's in-place sort does not leak between calls."""
    arr1 = [10, 2, 33]
    arr2 = [7, 7, 1]
    assert maximum(arr1, 2) == [10, 33]
    assert maximum(arr2, 1) == [7]
    # Each call only mutates its own argument.
    assert arr1 == [2, 10, 33]
    assert arr2 == [1, 7, 7]
