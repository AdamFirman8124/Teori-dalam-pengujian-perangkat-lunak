# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f090 import next_smallest


def test_next_smallest_returns_second_smallest():
    """With >= 2 distinct values, returns the second smallest (line 4, else branch)."""
    assert next_smallest([4, 1, 3, 2]) == 2
    assert next_smallest([5, 5, 1, 1, 3]) == 3  # duplicates removed by set()


def test_next_smallest_returns_none_for_fewer_than_two_distinct():
    """With < 2 distinct values, returns None (line 4, if branch)."""
    assert next_smallest([7]) is None
    assert next_smallest([]) is None
    assert next_smallest([2, 2, 2]) is None  # duplicates collapse to one element


def test_next_smallest_does_not_mutate_input():
    """Input list is not modified (sorted/set create new objects)."""
    original = [3, 1, 2]
    snapshot = list(original)
    next_smallest(original)
    assert original == snapshot
