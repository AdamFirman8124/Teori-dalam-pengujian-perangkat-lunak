# file: project/f034/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f034 import unique


def test_unique_removes_duplicates_and_sorts():
    """Duplicates are removed and the result is sorted ascending."""
    result = unique([3, 1, 2, 3, 1])
    assert result == [1, 2, 3]
    # Postcondition: result equals sorted set of the input
    assert result == sorted(set([3, 1, 2, 3, 1]))


def test_unique_empty_list():
    """An empty list yields an empty list."""
    assert unique([]) == []


def test_unique_already_unique_sorted():
    """A list with unique, already sorted elements is unchanged."""
    assert unique(["a", "b", "c"]) == ["a", "b", "c"]


def test_unique_negative_and_mixed_numbers():
    """Negative numbers and zero are handled and sorted correctly."""
    result = unique([0, -1, 0, -1, 5])
    assert result == [-1, 0, 5]
    assert result == sorted(set([0, -1, 0, -1, 5]))


def test_unique_does_not_mutate_input():
    """The input list is not mutated by the call."""
    original = [2, 1, 2]
    snapshot = list(original)
    result = unique(original)
    assert original == snapshot
    assert result == [1, 2]
