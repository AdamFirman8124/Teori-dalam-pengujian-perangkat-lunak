# file: project/f070/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}

from f070 import strange_sort_list


def test_strange_sort_list_alternates_min_and_max():
    values = [3, 1, 4, 2]

    result = strange_sort_list(values)

    assert result == [1, 4, 2, 3]
    assert values == []


def test_strange_sort_list_empty_input():
    values = []

    result = strange_sort_list(values)

    assert result == []
    assert values == []
