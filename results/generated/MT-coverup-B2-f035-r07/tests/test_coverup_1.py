# file: project/f035/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f035 import max_element


def test_max_element_max_at_end():
    result = max_element([1, 2, 3])
    assert result == 3


def test_max_element_max_at_start():
    result = max_element([5, 3, 1])
    assert result == 5


def test_max_element_single_element():
    result = max_element([42])
    assert result == 42


def test_max_element_with_duplicates():
    result = max_element([2, 7, 7, 3])
    assert result == 7


def test_max_element_negative_numbers():
    result = max_element([-5, -1, -3])
    assert result == -1
