# file: project/f152/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f152 import compare


def test_compare_returns_absolute_differences():
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 1, 5]
    result = compare(game, guess)
    assert result == [0, 0, 0, 0, 4, 4]
    assert len(result) == len(game)


def test_compare_handles_negative_differences():
    game = [5, 1, 10]
    guess = [1, 5, 3]
    result = compare(game, guess)
    assert result == [4, 4, 7]


def test_compare_empty_inputs():
    assert compare([], []) == []


def test_compare_mixed_types():
    game = [0, -2, 3.5]
    guess = [2, 2, 1.5]
    result = compare(game, guess)
    assert result == [2, 4, 2.0]
    assert all(isinstance(v, (int, float)) for v in result)
