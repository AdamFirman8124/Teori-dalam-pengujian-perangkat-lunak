# file: project/f152/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f152 import compare


def test_compare_basic_absolute_differences():
    """Line 3: list comprehension over zipped pairs, mixed exact/hit/miss."""
    game = [1, 2, 3, 4, 5]
    guess = [1, 3, 5, 3, 1]
    result = compare(game, guess)
    assert result == [0, 1, 2, 1, 4]
    # postcondition: every entry is a non-negative integer
    assert all(isinstance(d, int) and d >= 0 for d in result)


def test_compare_all_matches():
    """Exercise the x == y branch of abs(x - y): all zeros."""
    assert compare([5, 10, 15], [5, 10, 15]) == [0, 0, 0]


def test_compare_guess_below_game():
    """Exercise the y < x branch (negative difference becomes positive)."""
    assert compare([10, 20, 30], [1, 5, 15]) == [9, 15, 15]


def test_compare_guess_above_game():
    """Exercise the y > x branch (positive difference stays positive)."""
    assert compare([0, 0, 0], [3, 7, 11]) == [3, 7, 11]


def test_compare_empty_lists():
    """Edge case: zip of empty iterables yields an empty result list."""
    assert compare([], []) == []


def test_compare_single_elements():
    """Minimal non-empty input still executes the comprehension body."""
    assert compare([7], [2]) == [5]
    assert compare([2], [7]) == [5]


def test_compare_does_not_mutate_inputs():
    """Postcondition: inputs remain unchanged (function is pure)."""
    game = [1, 2, 3]
    guess = [4, 2, 0]
    original_game = list(game)
    original_guess = list(guess)
    compare(game, guess)
    assert game == original_game
    assert guess == original_guess
