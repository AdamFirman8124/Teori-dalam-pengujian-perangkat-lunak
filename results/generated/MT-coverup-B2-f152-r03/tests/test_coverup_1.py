# file: project/f152/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f152 import compare


def test_compare_returns_absolute_differences():
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 1, -1]
    result = compare(game, guess)
    assert result == [0, 0, 0, 0, 4, 2]
    assert all(isinstance(v, int) for v in result)


def test_compare_empty_inputs():
    assert compare([], []) == []


def test_compare_negative_differences():
    game = [10, -5, 0]
    guess = [3, 2, 7]
    assert compare(game, guess) == [7, 7, 7]
