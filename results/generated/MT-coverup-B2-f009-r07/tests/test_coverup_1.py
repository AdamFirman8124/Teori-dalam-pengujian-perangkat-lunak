# file: project/f009/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 10, 11, 13, 15, 17], "branches": [[9, 10], [9, 17], [10, 11], [10, 13]]}
# gained: {"lines": [6, 7, 9, 10, 11, 13, 15, 17], "branches": [[9, 10], [9, 17], [10, 11], [10, 13]]}

import pytest

from f009 import rolling_max


def test_rolling_max_empty_list():
    """Empty input: lines 6-7 and 17 execute, loop body never runs."""
    assert rolling_max([]) == []


def test_rolling_max_single_element():
    """Single element covers the 'running_max is None' branch (lines 10-11)."""
    assert rolling_max([7]) == [7]


def test_rolling_max_increasing():
    """Increasing sequence: every element becomes the new running max."""
    assert rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_rolling_max_decreasing():
    """Decreasing sequence: covers the else branch (line 13) with max keeping the old value."""
    assert rolling_max([5, 4, 3, 2]) == [5, 5, 5, 5]


def test_rolling_max_mixed():
    """Mixed sequence exercises both branches (lines 10-11 and 13) repeatedly."""
    assert rolling_max([3, 1, 4, 1, 5, 9, 2, 6]) == [3, 3, 4, 4, 5, 9, 9, 9]


def test_rolling_max_negative_numbers():
    """Negative values are handled correctly by the running max logic."""
    assert rolling_max([-5, -1, -3, -2]) == [-5, -1, -1, -1]


def test_rolling_max_duplicates():
    """Duplicates: max(running_max, n) returns the same value (line 13)."""
    assert rolling_max([2, 2, 2]) == [2, 2, 2]


def test_rolling_max_result_is_new_list():
    """Postcondition: the returned list is a fresh object, input is not mutated."""
    numbers = [1, 3, 2]
    result = rolling_max(numbers)
    assert result == [1, 3, 3]
    assert result is not numbers
    assert numbers == [1, 3, 2]
