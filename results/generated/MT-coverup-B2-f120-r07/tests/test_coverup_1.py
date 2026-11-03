# file: project/f120/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}

import pytest

from f120 import maximum


def test_maximum_k_zero_returns_empty_list():
    """Covers lines 3-4: the `k == 0` early-return branch."""
    arr = [3, 1, 2]
    result = maximum(arr, 0)
    assert result == []
    # k == 0 short-circuits before sorting, so the input must be untouched.
    assert arr == [3, 1, 2]


def test_maximum_positive_k_returns_top_k_in_ascending_order():
    """Covers lines 5-7: sort, slice, and return for k > 0."""
    arr = [5, 1, 3, 2, 4]
    result = maximum(arr, 3)
    # The function sorts its argument in place.
    assert arr == [1, 2, 3, 4, 5]
    assert result == [3, 4, 5]


def test_maximum_k_equal_to_length_returns_whole_sorted_array():
    arr = [10, -1, 7]
    result = maximum(arr, 3)
    assert result == [-1, 7, 10]


def test_maximum_handles_duplicates_and_negatives():
    arr = [2, -5, 2, 0]
    result = maximum(arr, 2)
    # After sorting: [-5, 0, 2, 2]; the last two elements are [2, 2].
    assert result == [2, 2]


def test_maximum_single_element_k_one():
    arr = [42]
    result = maximum(arr, 1)
    assert result == [42]
