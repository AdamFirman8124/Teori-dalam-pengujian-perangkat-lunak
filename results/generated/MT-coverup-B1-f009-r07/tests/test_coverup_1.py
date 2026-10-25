# file: project/f009/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 10, 11, 13, 15, 17], "branches": [[9, 10], [9, 17], [10, 11], [10, 13]]}
# gained: {"lines": [6, 7, 9, 10, 11, 13, 15, 17], "branches": [[9, 10], [9, 17], [10, 11], [10, 13]]}

import pytest

from f009 import rolling_max


def test_rolling_max_empty_list():
    """Covers lines 6-7 (initialization) and line 17 (return) with an empty input."""
    assert rolling_max([]) == []


def test_rolling_max_single_element():
    """Covers the 'running_max is None' branch (lines 10-11) with one element."""
    assert rolling_max([5]) == [5]


def test_rolling_max_increasing():
    """Covers the else branch (line 13) where each new element is larger."""
    assert rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_rolling_max_decreasing():
    """Covers the else branch (line 13) where max() keeps the previous value."""
    assert rolling_max([4, 3, 2, 1]) == [4, 4, 4, 4]


def test_rolling_max_mixed():
    """Covers both branches and verifies the full rolling-max postcondition."""
    numbers = [2, 5, 1, 3, 0, 8]
    expected = [2, 5, 5, 5, 5, 8]
    result = rolling_max(numbers)
    assert result == expected
    # Postcondition: result is non-decreasing and each entry is the max of the prefix.
    for i in range(len(numbers)):
        assert result[i] == max(numbers[: i + 1])
    assert result == sorted(result)


def test_rolling_max_with_negatives():
    """Covers both branches with negative numbers, including None-branch first element."""
    assert rolling_max([-3, -1, -7, -2]) == [-3, -1, -1, -1]


def test_rolling_max_does_not_mutate_input():
    """Ensures the function has no side effects on its argument (state-pollution check)."""
    numbers = [3, 1, 2]
    original = list(numbers)
    rolling_max(numbers)
    assert numbers == original
