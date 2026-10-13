# file: script_9.py:4-21
# asked: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}
# gained: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}

import pytest
from typing import List

# Import the function under test. Adjust the import if the module name differs.
try:
    from script_9 import rolling_max
except ImportError:
    from script_9 import rolling_max as _rm
    rolling_max = _rm


def test_rolling_max_nonempty_list():
    """Covers lines 10-21: the loop body executes, including both the
    'running_max is None' branch (first iteration) and the else branch."""
    numbers = [1, 2, 3, 2, 3, 4, 2]
    result = rolling_max(numbers)
    # Postconditions
    assert result == [1, 2, 3, 3, 3, 4, 4]
    assert len(result) == len(numbers)
    # Verify rolling-max invariant element-wise
    running = None
    for i, n in enumerate(numbers):
        running = n if running is None else max(running, n)
        assert result[i] == running


def test_rolling_max_empty_list():
    """Covers the case where the for loop body never executes (lines 13-19
    skipped), verifying the function returns an empty list."""
    assert rolling_max([]) == []


def test_rolling_max_single_element():
    """Covers only the 'running_max is None' branch (lines 14-15) once."""
    assert rolling_max([5]) == [5]


def test_rolling_max_decreasing_sequence():
    """Covers the else branch (line 17) repeatedly where running_max stays
    the same because every new element is smaller."""
    assert rolling_max([9, 7, 5, 3, 1]) == [9, 9, 9, 9, 9]


def test_rolling_max_increasing_sequence():
    """Covers the else branch (line 17) where running_max is updated to the
    new element each time."""
    assert rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_rolling_max_with_negatives_and_duplicates():
    """Covers both branches with negative numbers and duplicates."""
    numbers = [-1, -3, -1, -1, -5, 0]
    result = rolling_max(numbers)
    assert result == [-1, -1, -1, -1, -1, 0]


def test_rolling_max_does_not_mutate_input(monkeypatch):
    """Ensures the function does not mutate the input list (postcondition)."""
    numbers = [3, 1, 4, 1, 5]
    original = list(numbers)
    result = rolling_max(numbers)
    assert numbers == original
    assert result == [3, 3, 4, 4, 5]
