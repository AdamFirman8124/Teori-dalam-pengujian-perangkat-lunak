# file: project/f033/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f033 import sort_third


def test_sort_third_basic():
    result = sort_third([5, 6, 3, 4, 8, 9, 1])
    assert result == [1, 6, 3, 4, 8, 9, 5]


def test_sort_third_empty():
    assert sort_third([]) == []


def test_sort_third_short_lists():
    assert sort_third([1]) == [1]
    assert sort_third([2, 1]) == [2, 1]
    assert sort_third([3, 2, 1]) == [3, 2, 1]


def test_sort_third_does_not_mutate_and_accepts_tuple():
    orig = [9, 2, 1, 6, 5, 4, 3, 8, 7]
    snapshot = list(orig)
    result = sort_third(orig)
    assert result == [3, 2, 1, 6, 5, 4, 9, 8, 7]
    assert orig == snapshot
    assert result is not orig
    assert sort_third((5, 6, 3, 4)) == [4, 6, 3, 5]
