# file: project/f070/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}

import pytest

from f070 import strange_sort_list


def test_strange_sort_list_empty_returns_empty_and_leaves_list_empty():
    lst = []
    result = strange_sort_list(lst)
    assert result == []
    assert lst == []


def test_strange_sort_list_single_element():
    lst = [42]
    result = strange_sort_list(lst)
    assert result == [42]
    assert lst == []


def test_strange_sort_list_alternates_min_then_max():
    lst = [1, 2, 3, 4]
    result = strange_sort_list(lst)
    assert result == [1, 4, 2, 3]
    assert lst == []


def test_strange_sort_list_unsorted_input():
    lst = [5, 1, 9, 3, 7]
    result = strange_sort_list(lst)
    assert result == [1, 9, 3, 7, 5]
    assert lst == []


def test_strange_sort_list_with_duplicates():
    lst = [1, 1, 2]
    result = strange_sort_list(lst)
    assert result == [1, 2, 1]
    assert lst == []


def test_strange_sort_list_negative_numbers():
    lst = [-3, 0, -10, 4]
    result = strange_sort_list(lst)
    assert result == [-10, 4, -3, 0]
    assert lst == []


def test_strange_sort_list_does_not_touch_original_when_copied(monkeypatch):
    original = [3, 1, 2]
    snapshot = list(original)
    result = strange_sort_list(list(original))
    assert result == [1, 3, 2]
    assert original == snapshot


def test_strange_sort_list_result_is_sorted_by_alternating_extremes():
    lst = [8, 2, 6, 4, 0]
    result = strange_sort_list(lst)
    assert len(result) == 5
    assert sorted(result) == [0, 2, 4, 6, 8]
    assert result[0] == min([8, 2, 6, 4, 0])
    assert result[1] == max([8, 2, 6, 4, 0])
    assert lst == []
