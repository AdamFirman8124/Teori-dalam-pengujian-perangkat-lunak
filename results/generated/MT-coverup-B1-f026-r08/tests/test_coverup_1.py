# file: project/f026/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

from f026 import remove_duplicates


def test_remove_duplicates_empty():
    assert remove_duplicates([]) == []


def test_remove_duplicates_no_duplicates():
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]


def test_remove_duplicates_all_duplicates():
    assert remove_duplicates([1, 1, 2, 2]) == []


def test_remove_duplicates_mixed():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 3, 5]
