# file: project/f042/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f042 import incr_list


def test_incr_list_basic():
    """Calling incr_list executes line 3 and increments each element by 1."""
    result = incr_list([1, 2, 3])
    assert result == [2, 3, 4]


def test_incr_list_empty():
    """An empty list yields an empty list; line 3 still executes."""
    assert incr_list([]) == []


def test_incr_list_various_numeric_types():
    """Works with ints, floats, and negatives."""
    result = incr_list([0, -1, 2.5])
    assert result == [1, 0, 3.5]


def test_incr_list_does_not_mutate_input():
    """The input list is not modified (no state pollution)."""
    original = [1, 2, 3]
    snapshot = list(original)
    incr_list(original)
    assert original == snapshot
