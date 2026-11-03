# file: project/f070/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}

import pytest

from f070 import strange_sort_list


def test_strange_sort_list_alternating():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]


def test_strange_sort_list_single():
    assert strange_sort_list([5]) == [5]


def test_strange_sort_list_empty():
    assert strange_sort_list([]) == []


def test_strange_sort_list_duplicates():
    assert strange_sort_list([3, 3, 1]) == [1, 3, 3]
