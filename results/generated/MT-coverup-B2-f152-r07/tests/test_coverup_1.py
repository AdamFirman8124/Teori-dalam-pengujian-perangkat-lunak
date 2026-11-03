# file: project/f152/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f152 import compare


def test_compare_basic():
    """Execute line 3: the list comprehension computing absolute differences."""
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2, -2]
    result = compare(game, guess)
    assert result == [0, 0, 0, 0, 3, 3]
    assert isinstance(result, list)


def test_compare_all_equal():
    """When every guess matches, all differences are zero."""
    assert compare([0, 5, 10], [0, 5, 10]) == [0, 0, 0]


def test_compare_empty_inputs():
    """zip over empty sequences yields an empty result list."""
    assert compare([], []) == []


def test_compare_tuples_and_negative_values():
    """Works with any iterable pairs, including negative numbers."""
    assert compare((3, -4), (-3, 4)) == [6, 8]


def test_compare_result_length_matches_inputs():
    """Postcondition: output length equals the shorter input length."""
    game = [1, 2, 3, 4]
    guess = [4, 3, 2]
    result = compare(game, guess)
    assert len(result) == min(len(game), len(guess))
    assert result == [3, 1, 1]
