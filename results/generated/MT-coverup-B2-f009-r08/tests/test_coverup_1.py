# file: project/f009/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 10, 11, 13, 15, 17], "branches": [[9, 10], [9, 17], [10, 11], [10, 13]]}
# gained: {"lines": [6, 7, 9, 10, 11, 13, 15, 17], "branches": [[9, 10], [9, 17], [10, 11], [10, 13]]}

import pytest

from f009 import rolling_max


def test_rolling_max_empty_list():
    """Covers lines 6, 7 and 17 (loop never entered)."""
    assert rolling_max([]) == []


def test_rolling_max_single_element():
    """Covers lines 9, 10, 11 and 15 (first-iteration branch)."""
    assert rolling_max([7]) == [7]


def test_rolling_max_increasing():
    """Covers line 13 (else branch) with strictly increasing values."""
    assert rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_rolling_max_decreasing():
    """Covers line 13 with decreasing values (max keeps previous)."""
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]


def test_rolling_max_mixed():
    """Covers both branches of the if/else across a mixed sequence."""
    assert rolling_max([3, 1, 4, 1, 5, 2]) == [3, 3, 4, 4, 5, 5]


def test_rolling_max_with_duplicates():
    """Equal values still take the else branch (max of equal values)."""
    assert rolling_max([2, 2, 2]) == [2, 2, 2]


def test_rolling_max_negative_numbers():
    """Works correctly with negative values."""
    assert rolling_max([-5, -1, -3, -2]) == [-5, -1, -1, -1]


def test_rolling_max_does_not_mutate_input():
    """Postcondition: the input list is left unchanged."""
    numbers = [3, 1, 2]
    original = list(numbers)
    result = rolling_max(numbers)
    assert numbers == original
    assert result == [3, 3, 3]
    assert result is not numbers
