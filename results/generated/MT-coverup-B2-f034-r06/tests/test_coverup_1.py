# file: project/f034/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f034 import unique


def test_unique_returns_sorted_distinct_elements():
    result = unique([3, 1, 2, 3, 1])
    assert result == [1, 2, 3]


def test_unique_empty_list():
    assert unique([]) == []


def test_unique_already_sorted_no_duplicates():
    assert unique([1, 2, 3]) == [1, 2, 3]


def test_unique_negative_and_mixed_values():
    assert unique([-1, 5, -1, 0, 5]) == [-1, 0, 5]


def test_unique_does_not_mutate_input():
    original = [3, 1, 2]
    snapshot = list(original)
    unique(original)
    assert original == snapshot
