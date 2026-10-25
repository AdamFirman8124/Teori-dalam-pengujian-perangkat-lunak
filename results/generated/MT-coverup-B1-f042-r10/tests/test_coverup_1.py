# file: project/f042/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f042 import incr_list


def test_incr_list_empty():
    """Covers line 3 with an empty list input."""
    result = incr_list([])
    assert result == []
    assert result is not []


def test_incr_list_nonempty():
    """Covers line 3 with a non-empty list input."""
    result = incr_list([1, 2, 3])
    assert result == [2, 3, 4]


def test_incr_list_does_not_mutate_input():
    """Verifies the input list is not mutated (pure function)."""
    original = [1, 2, 3]
    snapshot = list(original)
    incr_list(original)
    assert original == snapshot


def test_incr_list_negative_and_zero():
    """Covers line 3 with negative numbers and zero."""
    result = incr_list([-1, 0, 1])
    assert result == [0, 1, 2]
