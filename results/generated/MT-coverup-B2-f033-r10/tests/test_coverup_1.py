# file: project/f033/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f033 import sort_third


def test_sort_third_sorts_every_third_item_without_mutating_input():
    original = (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

    result = sort_third(original)

    assert result == [0, 8, 7, 3, 5, 4, 6, 2, 1, 9]
    assert isinstance(result, list)
    assert original == (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
