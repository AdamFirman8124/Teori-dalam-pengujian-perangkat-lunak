# file: project/f152/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f152 import compare


def test_compare_identical_lists_returns_zeros():
    result = compare([1, 2, 3], [1, 2, 3])
    assert result == [0, 0, 0]
    assert len(result) == 3


def test_compare_different_values_returns_absolute_differences():
    result = compare([1, 2, 3], [4, 1, 6])
    assert result == [3, 1, 3]
    assert all(isinstance(v, int) for v in result)


def test_compare_negative_and_mixed_signs():
    result = compare([-5, 0, 7], [5, -3, 7])
    assert result == [10, 3, 0]


def test_compare_floats():
    result = compare([1.5, 2.25], [0.5, 4.0])
    assert result == pytest.approx([1.0, 1.75])


def test_compare_empty_lists_returns_empty_list():
    result = compare([], [])
    assert result == []
    assert isinstance(result, list)


def test_compare_unequal_lengths_truncates_to_shortest():
    result = compare([1, 2, 3, 4], [1, 2])
    assert result == [0, 0]
    assert len(result) == 2


def test_compare_does_not_mutate_inputs():
    game = [1, 2, 3]
    guess = [4, 5, 6]
    game_copy = list(game)
    guess_copy = list(guess)

    compare(game, guess)

    assert game == game_copy
    assert guess == guess_copy


def test_compare_returns_new_list_each_call():
    game = [1, 2, 3]
    guess = [1, 2, 3]

    first = compare(game, guess)
    second = compare(game, guess)

    assert first == second
    assert first is not second
    assert first is not game
