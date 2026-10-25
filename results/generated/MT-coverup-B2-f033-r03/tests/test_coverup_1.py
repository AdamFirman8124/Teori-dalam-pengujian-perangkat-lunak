# file: project/f033/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f033 import sort_third


def test_sort_third_basic_reorders_every_third():
    result = sort_third([5, 6, 3, 4, 8, 9, 2])
    assert result == [2, 6, 3, 4, 8, 9, 5]


def test_sort_third_empty_list():
    assert sort_third([]) == []


def test_sort_third_short_lists_unchanged():
    assert sort_third([1]) == [1]
    assert sort_third([3, 2]) == [3, 2]
    assert sort_third([1, 2, 3]) == [1, 2, 3]


def test_sort_third_four_elements():
    assert sort_third([9, 6, 3, 4]) == [4, 6, 3, 9]


def test_sort_third_does_not_mutate_input():
    original = [5, 6, 3, 4, 8, 9, 2]
    snapshot = list(original)
    result = sort_third(original)
    assert result == [2, 6, 3, 4, 8, 9, 5]
    assert original == snapshot
    assert result is not original


def test_sort_third_accepts_tuple_and_returns_list():
    result = sort_third((9, 1, 2, 3))
    assert result == [3, 1, 2, 9]
    assert isinstance(result, list)
