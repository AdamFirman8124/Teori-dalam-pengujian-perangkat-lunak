# file: project/f152/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f152.compare — ensures line 3 (the list comprehension) executes.

compare() is a pure function, so no monkeypatching/teardown is required;
the final test additionally verifies that it does not mutate its inputs,
guarding against state pollution.
"""

import pytest

from f152 import compare


def test_compare_returns_absolute_differences():
    """Exercise line 3: zip pairs elements and abs() handles both signs."""
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 5, -1]
    result = compare(game, guess)
    assert result == [0, 0, 0, 0, 0, 2]
    assert all(isinstance(d, int) for d in result)


def test_compare_mixed_signs():
    """abs() must map negative differences to positive values."""
    assert compare([3, -1, 0], [1, 2, 5]) == [2, 3, 5]


def test_compare_empty_inputs():
    """zip over empty sequences yields an empty comprehension result."""
    assert compare([], []) == []


def test_compare_unequal_lengths_stops_at_shorter():
    """zip truncates to the shorter input; line 3 must not raise."""
    assert compare([1, 2, 3], [10]) == [9]


def test_compare_does_not_mutate_inputs():
    """The comprehension must not mutate its arguments (no state pollution)."""
    game = [1, 2]
    guess = [3, 4]
    compare(game, guess)
    assert game == [1, 2]
    assert guess == [3, 4]
