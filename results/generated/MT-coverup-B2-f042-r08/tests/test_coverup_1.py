# file: project/f042/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f042 import incr_list


def test_incr_list_increments_each_element():
    result = incr_list([1, 2, 3])
    assert result == [2, 3, 4]


def test_incr_list_empty_list():
    result = incr_list([])
    assert result == []


def test_incr_list_does_not_mutate_input():
    original = [0, 5, 10]
    snapshot = list(original)
    result = incr_list(original)
    assert original == snapshot
    assert result == [1, 6, 11]
