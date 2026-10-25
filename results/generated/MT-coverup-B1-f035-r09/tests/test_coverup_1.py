# file: project/f035/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f035 import max_element


def test_max_element_returns_last_when_sorted_ascending():
    result = max_element([1, 2, 3, 4])
    assert result == 4


def test_max_element_returns_first_when_sorted_descending():
    result = max_element([4, 3, 2, 1])
    assert result == 4


def test_max_element_updates_when_larger_element_found():
    result = max_element([3, 7, 2, 9, 5])
    assert result == 9


def test_max_element_single_element():
    result = max_element([42])
    assert result == 42


def test_max_element_negative_numbers():
    result = max_element([-5, -1, -9])
    assert result == -1


def test_max_element_with_duplicates():
    result = max_element([2, 2, 2])
    assert result == 2
