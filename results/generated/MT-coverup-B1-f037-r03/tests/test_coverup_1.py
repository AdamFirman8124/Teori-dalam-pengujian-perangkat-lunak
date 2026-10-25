# file: project/f037/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

import pytest

from f037 import sort_even


def test_sort_even_equal_lengths():
    result = sort_even([4, 1, 2, 3])
    assert result == [2, 1, 4, 3]


def test_sort_even_extra_even_element():
    result = sort_even([5, 1, 3, 2, 4])
    assert result == [3, 1, 4, 2, 5]


def test_sort_even_empty_list():
    assert sort_even([]) == []


def test_sort_even_single_element():
    assert sort_even([7]) == [7]


def test_sort_even_does_not_mutate_input():
    original = [3, 1, 2, 4]
    sort_even(original)
    assert original == [3, 1, 2, 4]
