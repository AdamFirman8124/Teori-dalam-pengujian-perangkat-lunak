# file: project/f034/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f034 import unique


def test_unique_empty_list():
    assert unique([]) == []


def test_unique_removes_duplicates_and_sorts():
    data = [3, 1, 2, 1, 3, 2]
    result = unique(data)
    assert result == [1, 2, 3]
    assert data == [3, 1, 2, 1, 3, 2]


def test_unique_already_unique_sorted():
    assert unique([1, 2, 3]) == [1, 2, 3]


def test_unique_strings():
    assert unique(["b", "a", "b", "c", "a"]) == ["a", "b", "c"]


def test_unique_single_and_negative_values():
    assert unique([5]) == [5]
    assert unique([0, -1, 2, -1, 0]) == [-1, 0, 2]
