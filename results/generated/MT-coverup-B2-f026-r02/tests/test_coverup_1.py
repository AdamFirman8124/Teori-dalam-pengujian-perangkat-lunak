# file: project/f026/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import pytest

from f026 import remove_duplicates


def test_remove_duplicates_no_duplicates():
    """All elements unique: every element is kept (lines 6-8 execute)."""
    result = remove_duplicates([1, 2, 3])
    assert result == [1, 2, 3]


def test_remove_duplicates_with_duplicates():
    """Elements appearing more than once are removed entirely."""
    result = remove_duplicates([1, 2, 2, 3, 3, 3, 4])
    assert result == [1, 4]


def test_remove_duplicates_empty_list():
    """Empty input yields empty output."""
    assert remove_duplicates([]) == []


def test_remove_duplicates_all_duplicates():
    """All elements duplicated: nothing is kept."""
    assert remove_duplicates([7, 7, 7]) == []


def test_remove_duplicates_preserves_order():
    """Order of surviving elements follows original order."""
    result = remove_duplicates([5, 1, 5, 2, 1, 3])
    assert result == [2, 3]


def test_remove_duplicates_does_not_mutate_input():
    """The input list is not modified by the function."""
    numbers = [1, 1, 2, 3]
    original = list(numbers)
    remove_duplicates(numbers)
    assert numbers == original
