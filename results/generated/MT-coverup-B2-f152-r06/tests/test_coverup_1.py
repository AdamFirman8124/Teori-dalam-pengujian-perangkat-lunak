# file: project/f152/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f152 import compare


def test_compare_basic():
    """Covers line 3 (the list comprehension) with typical inputs."""
    result = compare([1, 2, 3], [4, 5, 6])
    assert result == [3, 3, 3]
    assert all(isinstance(v, int) for v in result)


def test_compare_negative_differences():
    """Ensures abs() is applied: order of arguments does not matter."""
    assert compare([1, 5, 0], [3, 2, 7]) == [2, 3, 7]
    assert compare([3, 2, 7], [1, 5, 0]) == [2, 3, 7]


def test_compare_equal_elements():
    """Zero differences are handled correctly."""
    assert compare([4, 4, 4], [4, 4, 4]) == [0, 0, 0]


def test_compare_empty_sequences():
    """Empty inputs still execute the return statement (line 3)."""
    assert compare([], []) == []


def test_compare_different_lengths():
    """zip() truncates to the shorter sequence."""
    assert compare([1, 2, 3], [10]) == [9]


def test_compare_symmetry():
    """compare(a, b) == compare(b, a) for arbitrary values."""
    game = [0, -1, 100, 7]
    guess = [5, 3, -50, 7]
    assert compare(game, guess) == compare(guess, game)
