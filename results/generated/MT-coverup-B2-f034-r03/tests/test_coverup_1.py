# file: project/f034/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f034.unique.

The module under test is:

    def unique(l: list):
        return sorted(list(set(l)))

Coverage reported that line 3 (the ``return`` statement) never executed,
which means the function was never called by the test suite.  The tests
below call ``unique`` with a variety of inputs so that line 3 (and the
whole function body, which contains no branches) is fully covered.

``unique`` is a pure function: it performs no I/O, mutates no module
state, and does not mutate its argument, so no monkeypatching or fixture
cleanup is required to avoid state pollution.
"""

import pytest

from f034 import unique


def test_unique_removes_duplicates_and_sorts():
    """Duplicates are removed and the result is sorted ascending."""
    result = unique([3, 1, 2, 3, 1, 2])
    assert result == [1, 2, 3]
    assert isinstance(result, list)


def test_unique_empty_list():
    """An empty input yields an empty list."""
    assert unique([]) == []


def test_unique_single_element():
    """A single-element input is returned unchanged."""
    assert unique([42]) == [42]


def test_unique_already_sorted_no_duplicates():
    """Already-sorted, duplicate-free input is returned unchanged."""
    assert unique([1, 2, 3]) == [1, 2, 3]


def test_unique_strings():
    """Works for hashable, orderable non-numeric items such as strings."""
    assert unique(["b", "a", "c", "a"]) == ["a", "b", "c"]


def test_unique_negative_numbers():
    """Handles negative numbers and zero correctly."""
    assert unique([-1, 5, -1, 0, 5]) == [-1, 0, 5]


def test_unique_does_not_mutate_input():
    """The input list is left untouched (set() does not mutate it)."""
    original = [3, 1, 2, 3]
    snapshot = list(original)
    result = unique(original)
    assert original == snapshot
    assert result == [1, 2, 3]
