# file: project/f034/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f034 import unique


def test_unique_removes_duplicates_and_sorts():
    result = unique([3, 1, 2, 3, 1])
    # Postcondition: duplicates removed and result is sorted ascending
    assert result == [1, 2, 3]
    assert result == sorted(set(result))


def test_unique_empty_list():
    assert unique([]) == []


def test_unique_already_sorted_unique_input():
    assert unique(["a", "b", "c"]) == ["a", "b", "c"]
