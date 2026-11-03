# file: project/f026/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import pytest

from f026 import remove_duplicates


def test_removes_all_occurrences_of_duplicates():
    # Duplicated values should be filtered out entirely (c[n] > 1 branch).
    numbers = [1, 2, 2, 3, 3, 3, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 4]
    # The input list must not be mutated by the function.
    assert numbers == [1, 2, 2, 3, 3, 3, 4]


def test_no_duplicates_keeps_all_elements_in_order():
    # All counts are 1, so the c[n] <= 1 branch is taken for every element.
    numbers = [3, 1, 4, 1, 5]
    result = remove_duplicates(numbers)
    # Only 3, 4, 5 occur exactly once, and order is preserved.
    assert result == [3, 4, 5]


def test_empty_list_returns_empty_list():
    # Covers Counter on an empty iterable and the comprehension yielding nothing.
    assert remove_duplicates([]) == []


def test_all_duplicates_returns_empty_list():
    # Every element has count > 1, so nothing passes the filter.
    assert remove_duplicates([7, 7, 7]) == []


def test_returns_new_list_even_when_unchanged():
    # Ensures the comprehension builds a fresh list rather than aliasing input.
    numbers = [1, 2, 3]
    result = remove_duplicates(numbers)
    assert result == numbers
    assert result is not numbers
