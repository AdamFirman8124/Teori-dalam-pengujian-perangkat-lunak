# file: project/f152/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f152 import compare


def test_compare_returns_absolute_differences():
    game = [1, 2, 3, 4, 5]
    guess = [1, 3, 3, 3, 5]
    result = compare(game, guess)
    assert result == [0, 1, 0, 1, 0]
    assert isinstance(result, list)
    assert len(result) == len(game)


def test_compare_empty_inputs_return_empty_list():
    assert compare([], []) == []


def test_compare_truncates_to_shortest_input():
    # zip stops at the shortest iterable
    assert compare([1, 2, 3], [1, 2]) == [0, 0]
    assert compare([1], [1, 2, 3]) == [0]


def test_compare_handles_negative_values_and_floats():
    result = compare([-1, -5, 0.5], [1, -2, 0.25])
    assert result == pytest.approx([2, 3, 0.25])


def test_compare_accepts_arbitrary_iterables():
    assert compare((1, 2, 3), iter([3, 2, 1])) == [2, 0, 2]


def test_compare_does_not_mutate_inputs():
    game = [1, 2, 3]
    guess = [4, 5, 6]
    game_copy, guess_copy = list(game), list(guess)
    compare(game, guess)
    assert game == game_copy
    assert guess == guess_copy
