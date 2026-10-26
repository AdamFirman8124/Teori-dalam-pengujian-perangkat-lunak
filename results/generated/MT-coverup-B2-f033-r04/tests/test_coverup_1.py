# file: project/f033/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f033 import sort_third


def test_sort_third_sorts_every_third_item_without_mutating_input():
    original = [5, 1, 2, 4, 3, 0, 1]

    result = sort_third(original)

    assert result == [1, 1, 2, 4, 3, 0, 5]
    assert original == [5, 1, 2, 4, 3, 0, 1]
    assert result is not original


def test_sort_third_accepts_non_list_iterables():
    source = (9, 8, 7, 6)

    result = sort_third(source)

    assert result == [6, 8, 7, 9]
    assert isinstance(result, list)
    assert source == (9, 8, 7, 6)
