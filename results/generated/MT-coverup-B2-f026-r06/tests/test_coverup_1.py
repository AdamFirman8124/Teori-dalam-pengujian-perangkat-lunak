# file: project/f026/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import pytest

from f026 import remove_duplicates


def test_remove_duplicates_mixed():
    """Elements appearing more than once are removed entirely; unique ones kept."""
    numbers = [1, 2, 2, 3, 3, 3, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 4]
    # Original input must not be mutated.
    assert numbers == [1, 2, 2, 3, 3, 3, 4]


def test_remove_duplicates_all_unique():
    """A list with no duplicates is returned unchanged (same order)."""
    numbers = [5, 1, 9]
    assert remove_duplicates(numbers) == [5, 1, 9]


def test_remove_duplicates_all_duplicates():
    """A list where every element repeats yields an empty list."""
    assert remove_duplicates([7, 7, 7]) == []


def test_remove_duplicates_empty():
    """An empty list yields an empty list."""
    assert remove_duplicates([]) == []


def test_remove_duplicates_negative_and_zero():
    """Works with zero and negative integers."""
    numbers = [0, -1, 0, -1, 2]
    assert remove_duplicates(numbers) == [2]
