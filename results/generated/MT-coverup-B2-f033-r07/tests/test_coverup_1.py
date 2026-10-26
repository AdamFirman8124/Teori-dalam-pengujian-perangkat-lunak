# file: project/f033/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f033 import sort_third


def test_sort_third_sorts_every_third():
    assert sort_third([5, 6, 3, 4, 8, 9, 1, 2, 3]) == [1, 6, 3, 4, 8, 9, 5, 2, 3]


def test_sort_third_empty_and_short():
    assert sort_third([]) == []
    assert sort_third([1]) == [1]
    assert sort_third([3, 2, 1]) == [3, 2, 1]


def test_sort_third_does_not_mutate_and_accepts_iterable():
    orig = [5, 6, 3, 4, 8, 9, 1]
    orig_copy = list(orig)
    result = sort_third(orig)
    assert result == [1, 6, 3, 4, 8, 9, 5]
    assert orig == orig_copy
    assert result is not orig
    assert sort_third((3, 2, 1, 0)) == [0, 2, 1, 3]
