# file: project/f152/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f152 import compare


def test_compare_basic_differences():
    """Executes line 3: the list comprehension over zip(game, guess)."""
    result = compare([1, 2, 3], [4, 5, 3])
    assert result == [3, 3, 0]


def test_compare_absolute_value():
    """abs() must be applied, so argument order does not change the result."""
    assert compare([5, 1], [1, 5]) == [4, 4]
    assert compare([1, 5], [5, 1]) == [4, 4]


def test_compare_empty_sequences():
    """Empty inputs still execute the comprehension (line 3) and yield []."""
    assert compare([], []) == []


def test_compare_unequal_lengths():
    """zip stops at the shorter sequence; only paired elements are compared."""
    assert compare([1, 2, 3], [10]) == [9]
    assert compare([7], [2, 20, 30]) == [5]


def test_compare_zero_and_negative_values():
    """Handles zeros and negative numbers correctly."""
    assert compare([0, -3, 10], [0, 3, -10]) == [0, 6, 20]
