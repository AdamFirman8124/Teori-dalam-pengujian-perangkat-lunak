# file: project/f034/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f034 import unique


def test_unique_removes_duplicates_and_sorts():
    """Calling unique executes line 3 (the return statement) and
    verifies that duplicates are removed and the result is sorted."""
    result = unique([3, 1, 2, 3, 1])
    # Postcondition: duplicates removed
    assert len(result) == len(set(result))
    # Postcondition: elements match the expected unique values
    assert result == [1, 2, 3]
    # Postcondition: result is sorted
    assert result == sorted(result)


def test_unique_empty_list():
    """Edge case: empty input returns an empty list."""
    assert unique([]) == []


def test_unique_single_element():
    """Edge case: single-element list is returned unchanged."""
    assert unique([42]) == [42]


def test_unique_does_not_mutate_input():
    """Postcondition: the input list is not mutated by the call."""
    original = [2, 1, 2]
    snapshot = list(original)
    unique(original)
    assert original == snapshot
