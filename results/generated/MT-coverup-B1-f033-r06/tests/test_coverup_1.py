# file: project/f033/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f033 import sort_third


def test_sort_third_sorts_every_third_element():
    original = [5, 6, 3, 4, 8, 9, 1, 2, 3]
    snapshot = list(original)

    result = sort_third(original)

    assert result == [1, 6, 3, 4, 8, 9, 5, 2, 3]
    assert original == snapshot
    assert result is not original


def test_sort_third_empty_list():
    assert sort_third([]) == []


def test_sort_third_single_element():
    assert sort_third([42]) == [42]


def test_sort_third_preserves_non_third_elements():
    assert sort_third([9, 100, 200, 3, 300, 400, 6]) == [3, 100, 200, 6, 300, 400, 9]


def test_sort_third_accepts_tuple_and_returns_list():
    result = sort_third((3, 2, 1, 0))

    assert result == [0, 2, 1, 3]
    assert isinstance(result, list)


def test_sort_third_already_sorted():
    assert sort_third([1, 9, 8, 2, 7, 6, 3]) == [1, 9, 8, 2, 7, 6, 3]
