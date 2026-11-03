# file: project/f034/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f034 import unique


def test_unique_removes_duplicates_and_sorts():
    """Calling unique executes line 3 and returns a sorted list of unique elements."""
    result = unique([3, 1, 2, 3, 1])
    assert result == [1, 2, 3]
    # Postcondition: result equals sorted set of the input
    assert result == sorted(set([3, 1, 2, 3, 1]))
    # Postcondition: no duplicates
    assert len(result) == len(set(result))


def test_unique_empty_list():
    """Edge case: empty input yields empty output."""
    assert unique([]) == []


def test_unique_strings():
    """Works with non-numeric, hashable elements."""
    result = unique(["b", "a", "b", "c"])
    assert result == ["a", "b", "c"]
    assert result == sorted(set(["b", "a", "b", "c"]))


def test_unique_does_not_mutate_input():
    """The input list is left unchanged (function is pure)."""
    original = [2, 1, 2]
    snapshot = list(original)
    result = unique(original)
    assert original == snapshot
    assert result == [1, 2]
