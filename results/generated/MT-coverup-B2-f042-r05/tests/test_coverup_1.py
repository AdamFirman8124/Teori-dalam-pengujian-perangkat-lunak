# file: project/f042/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f042 import incr_list


def test_incr_list_basic():
    """Cover line 3: the list comprehension return, with a non-empty list."""
    result = incr_list([1, 2, 3])
    assert result == [2, 3, 4]


def test_incr_list_empty():
    """Cover line 3 with an empty list (comprehension body never runs)."""
    result = incr_list([])
    assert result == []


def test_incr_list_negative_and_floats():
    """Cover line 3 with mixed numeric values."""
    result = incr_list([-1, 0.5, 99])
    assert result == [0, 1.5, 100]


def test_incr_list_does_not_mutate_input():
    """Cover line 3 and verify the input list is not mutated."""
    original = [10, 20, 30]
    snapshot = list(original)
    result = incr_list(original)
    assert result == [11, 21, 31]
    assert original == snapshot
