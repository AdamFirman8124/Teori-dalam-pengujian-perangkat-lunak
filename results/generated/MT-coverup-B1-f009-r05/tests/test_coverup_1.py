# file: project/f009/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 10, 11, 13, 15, 17], "branches": [[9, 10], [9, 17], [10, 11], [10, 13]]}
# gained: {"lines": [6, 7, 9, 10, 11, 13, 15, 17], "branches": [[9, 10], [9, 17], [10, 11], [10, 13]]}

import pytest

from f009 import rolling_max


def test_rolling_max_empty_list():
    """Covers lines 6-7 and 17: initialization and return with an empty input."""
    assert rolling_max([]) == []


def test_rolling_max_single_element():
    """Covers the running_max is None branch (lines 10-11) with one element."""
    assert rolling_max([5]) == [5]


def test_rolling_max_increasing():
    """Covers the else branch (line 13) where each new element is larger."""
    assert rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_rolling_max_decreasing():
    """Covers the else branch (line 13) where max keeps the earlier value."""
    assert rolling_max([4, 3, 2, 1]) == [4, 4, 4, 4]


def test_rolling_max_mixed():
    """Covers both branches (lines 10-11 and 13) plus append (line 15)."""
    assert rolling_max([3, 1, 4, 1, 5, 9, 2, 6]) == [3, 3, 4, 4, 5, 9, 9, 9]


def test_rolling_max_with_negatives():
    """Covers both branches with negative values."""
    assert rolling_max([-5, -1, -10, 0]) == [-5, -1, -1, 0]


def test_rolling_max_does_not_mutate_input():
    """Postcondition: the input list is left unchanged."""
    numbers = [2, 7, 1]
    rolling_max(numbers)
    assert numbers == [2, 7, 1]


def test_rolling_max_result_length_matches_input():
    """Postcondition: output length equals input length."""
    numbers = [10, 3, 8, 8, 1]
    result = rolling_max(numbers)
    assert len(result) == len(numbers)
