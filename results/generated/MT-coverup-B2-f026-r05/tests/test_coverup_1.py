# file: project/f026/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

from f026 import remove_duplicates


def test_remove_duplicates_all_unique():
    result = remove_duplicates([1, 2, 3])
    assert result == [1, 2, 3]


def test_remove_duplicates_with_duplicates():
    result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
    assert result == [1, 3, 5]


def test_remove_duplicates_empty():
    result = remove_duplicates([])
    assert result == []


def test_remove_duplicates_all_duplicated():
    result = remove_duplicates([1, 1, 2, 2])
    assert result == []


def test_remove_duplicates_preserves_order():
    result = remove_duplicates([3, 1, 2, 1, 3, 4])
    assert result == [2, 4]
