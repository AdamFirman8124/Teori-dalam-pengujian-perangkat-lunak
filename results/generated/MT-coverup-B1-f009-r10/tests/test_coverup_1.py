# file: project/f009/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 10, 11, 13, 15, 17], "branches": [[9, 10], [9, 17], [10, 11], [10, 13]]}
# gained: {"lines": [6, 7, 9, 10, 11, 13, 15, 17], "branches": [[9, 10], [9, 17], [10, 11], [10, 13]]}

import pytest

from f009 import rolling_max


def test_rolling_max_empty_list():
    result = rolling_max([])
    assert result == []
    assert isinstance(result, list)


def test_rolling_max_single_element():
    result = rolling_max([5])
    assert result == [5]


def test_rolling_max_increasing():
    result = rolling_max([1, 2, 3, 4])
    assert result == [1, 2, 3, 4]


def test_rolling_max_decreasing():
    result = rolling_max([4, 3, 2, 1])
    assert result == [4, 4, 4, 4]


def test_rolling_max_mixed_values():
    result = rolling_max([3, 1, 4, 1, 5, 9, 2, 6])
    assert result == [3, 3, 4, 4, 5, 9, 9, 9]


def test_rolling_max_with_negatives_and_zero():
    result = rolling_max([-5, -2, -10, 0, -1])
    assert result == [-5, -2, -2, 0, 0]


def test_rolling_max_does_not_mutate_input():
    numbers = [2, 7, 1, 8]
    snapshot = list(numbers)
    result = rolling_max(numbers)
    assert numbers == snapshot
    assert result == [2, 7, 7, 8]
    assert result is not numbers


def test_rolling_max_returns_new_list_each_call():
    first = rolling_max([1, 2])
    second = rolling_max([1, 2])
    assert first == second
    assert first is not second
