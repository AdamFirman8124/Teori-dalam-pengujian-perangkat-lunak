# file: project/f034/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f034 import unique


def test_unique_removes_duplicates_and_sorts():
    """Line 3: deduplicates the input and returns elements in sorted order."""
    result = unique([3, 1, 2, 3, 1])
    assert result == [1, 2, 3]
    # Postcondition: result is sorted
    assert result == sorted(result)
    # Postcondition: no duplicates
    assert len(result) == len(set(result))


def test_unique_empty_list():
    """Line 3: handles the empty list edge case."""
    assert unique([]) == []


def test_unique_single_element():
    """Line 3: handles a single-element list."""
    assert unique([5]) == [5]


def test_unique_does_not_mutate_input():
    """Line 3: the input list is left unchanged (set/sorted build new objects)."""
    original = [3, 1, 2, 3]
    snapshot = list(original)
    result = unique(original)
    assert original == snapshot
    assert result == [1, 2, 3]
    # The result must be a new list, not the input object itself
    assert result is not original


def test_unique_strings():
    """Line 3: works with string elements (homogeneous, comparable types)."""
    result = unique(["b", "a", "b", "a"])
    assert result == ["a", "b"]
    assert result == sorted(result)
    assert len(result) == len(set(result))


def test_unique_negative_numbers():
    """Line 3: works with negative numbers and floats."""
    result = unique([-1.5, 2, -1.5, 0, 2])
    assert result == [-1.5, 0, 2]
    assert result == sorted(result)
