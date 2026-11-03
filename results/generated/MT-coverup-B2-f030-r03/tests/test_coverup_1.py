# file: project/f030/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f030.get_positive.

These tests execute line 3 (the list comprehension) and cover both
branches of the `if e > 0` filter, as well as the empty-iteration path.
The function under test is pure, so no state cleanup/monkeypatching is
required.
"""

from f030 import get_positive


def test_get_positive_mixed():
    """Mixed input exercises the comprehension loop with both branch outcomes
    of the `e > 0` condition (True for positives, False for negatives/zero)."""
    result = get_positive([1, -2, 3, 0, 4])
    assert result == [1, 3, 4]


def test_get_positive_empty_list():
    """Empty input covers the path where the comprehension loop body never runs."""
    assert get_positive([]) == []


def test_get_positive_all_non_positive():
    """All elements fail the `e > 0` condition (only the False branch taken)."""
    assert get_positive([-1, -5, 0]) == []


def test_get_positive_all_positive():
    """All elements pass the `e > 0` condition (only the True branch taken)."""
    assert get_positive([7, 8]) == [7, 8]


def test_get_positive_does_not_mutate_input():
    """Verifies the postcondition that the input list is left unmodified."""
    original = [1, -2, 3]
    snapshot = list(original)
    result = get_positive(original)
    assert original == snapshot
    assert result == [1, 3]
    assert result is not original
