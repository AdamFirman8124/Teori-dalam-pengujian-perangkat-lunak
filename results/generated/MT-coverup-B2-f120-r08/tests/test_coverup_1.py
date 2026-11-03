# file: project/f120/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}

from f120 import maximum


def test_maximum_k_zero_returns_empty_list():
    """Exercises lines 3-4: the k == 0 early-return branch."""
    arr = [3, 1, 2]
    result = maximum(arr, 0)
    assert result == []


def test_maximum_positive_k_returns_k_largest_in_ascending_order():
    """Exercises lines 5-7: sort, slice, and return for k > 0."""
    arr = [5, 1, 3, 2, 4]
    result = maximum(arr, 3)
    assert result == [3, 4, 5]
    # The function sorts the input list in place as a side effect.
    assert arr == [1, 2, 3, 4, 5]


def test_maximum_k_equals_len_returns_whole_sorted_list():
    """Exercises lines 5-7 with k == len(arr)."""
    arr = [2, 1]
    result = maximum(arr, 2)
    assert result == [1, 2]
    assert arr == [1, 2]
