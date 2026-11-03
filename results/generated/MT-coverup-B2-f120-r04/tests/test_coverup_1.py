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
    # Input list must not have been mutated on the early-return path.
    assert arr == [3, 1, 2]


def test_maximum_k_positive_returns_last_k_after_sort():
    """Covers lines 5-7: sort, slice, and return for k > 0."""
    arr = [5, 1, 9, 3]
    result = maximum(arr, 2)
    # After sorting, arr[-2:] yields the two largest elements in
    # ascending order: [5, 9].
    assert result == [5, 9]
    # arr.sort() mutates the caller's list; verify the side effect.
    assert arr == [1, 3, 5, 9]


def test_maximum_k_equals_len_returns_whole_sorted_list():
    """Covers lines 5-7 with k == len(arr) (slice covers everything)."""
    arr = [2, 7, 4]
    result = maximum(arr, 3)
    assert result == [2, 4, 7]
    assert arr == [2, 4, 7]


def test_maximum_does_not_pollute_state(monkeypatch):
    """Ensure repeated calls with fresh inputs behave independently
    (the function mutates its argument, so each call gets its own list)."""
    first = maximum([4, 2, 6], 1)
    second = maximum([4, 2, 6], 1)
    assert first == [6]
    assert second == [6]
