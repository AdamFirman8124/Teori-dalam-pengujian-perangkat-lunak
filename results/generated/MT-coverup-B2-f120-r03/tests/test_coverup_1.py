# file: project/f120/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}

import pytest

from f120 import maximum


def test_maximum_k_zero_returns_empty_list():
    """Covers line 3 (branch True) and line 4: k == 0 short-circuits to []."""
    arr = [3, 1, 2]
    result = maximum(arr, 0)
    assert result == []
    # Early return means the input list must NOT have been sorted/mutated.
    assert arr == [3, 1, 2]


def test_maximum_positive_k_returns_largest_k_sorted():
    """Covers line 3 (branch False), line 5 (arr.sort), line 6 (slice), line 7."""
    arr = [5, 1, 3, 2, 4]
    result = maximum(arr, 3)
    assert result == [3, 4, 5]
    # arr.sort() mutates the caller's list; verify the documented side effect.
    assert arr == [1, 2, 3, 4, 5]


def test_maximum_k_equal_to_length_returns_whole_sorted_array():
    """Edge case: k == len(arr); slice arr[-k:] yields the entire sorted list."""
    arr = [9, -1, 0]
    result = maximum(arr, 3)
    assert result == [-1, 0, 9]
    assert arr == [-1, 0, 9]


def test_maximum_single_element():
    """Minimal non-zero-k case exercising every line of the happy path."""
    arr = [7]
    result = maximum(arr, 1)
    assert result == [7]
    assert arr == [7]


def test_maximum_does_not_pollute_shared_state():
    """Each call works independently on its own input (no cross-test leakage)."""
    a = [2, 1]
    b = [10, 30, 20]
    assert maximum(a, 1) == [2]
    assert maximum(b, 2) == [20, 30]
    # Original objects were only mutated by sort(), never replaced or shared.
    assert a == [1, 2]
    assert b == [10, 20, 30]
