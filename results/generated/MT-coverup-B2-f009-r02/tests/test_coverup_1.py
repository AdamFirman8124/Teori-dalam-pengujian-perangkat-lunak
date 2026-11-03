# file: project/f009/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 10, 11, 13, 15, 17], "branches": [[9, 10], [9, 17], [10, 11], [10, 13]]}
# gained: {"lines": [6, 7, 9, 10, 11, 13, 15, 17], "branches": [[9, 10], [9, 17], [10, 11], [10, 13]]}

import pytest

from f009 import rolling_max


def test_rolling_max_multiple_elements():
    """Covers lines 6-17: initialization, loop, both branches of the
    'running_max is None' check (first iteration vs. later iterations),
    append, and return."""
    assert rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]


def test_rolling_max_single_element():
    """Covers the loop body executing exactly once (only the
    'running_max is None' branch)."""
    assert rolling_max([7]) == [7]


def test_rolling_max_empty_list():
    """Covers the loop-not-taken branch: result stays empty."""
    assert rolling_max([]) == []


def test_rolling_max_decreasing_sequence():
    """Running max must stay at the initial peak for a decreasing list."""
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]


def test_rolling_max_negative_numbers():
    """Correct behavior with negative values (max, not min)."""
    assert rolling_max([-3, -1, -7, -2]) == [-3, -1, -1, -1]


def test_rolling_max_does_not_mutate_input():
    """Postcondition: the input list is left untouched."""
    numbers = [2, 1, 3]
    snapshot = list(numbers)
    rolling_max(numbers)
    assert numbers == snapshot
