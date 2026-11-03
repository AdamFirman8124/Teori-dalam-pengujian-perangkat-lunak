# file: project/f034/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f034 import unique


def test_unique_removes_duplicates_and_sorts():
    """Executes line 3: unique must return the sorted list of distinct elements."""
    data = [3, 1, 2, 3, 1, 2]
    result = unique(data)
    # Postcondition: duplicates removed and result sorted ascending
    assert result == [1, 2, 3]
    assert result == sorted(set(data))
    assert len(result) == len(set(data))
    # The pure function must not mutate its input (no state pollution)
    assert data == [3, 1, 2, 3, 1, 2]


def test_unique_empty_list():
    """Edge case: empty input still exercises line 3."""
    assert unique([]) == []


def test_unique_already_sorted_unique_input():
    """Idempotence: input already unique and sorted is returned unchanged."""
    assert unique([1, 2, 3]) == [1, 2, 3]


def test_unique_negative_numbers_and_strings():
    """Works for negatives and non-numeric comparable types."""
    assert unique([-2, 5, -2, 0, 5]) == [-2, 0, 5]
    assert unique(["b", "a", "b", "a"]) == ["a", "b"]
