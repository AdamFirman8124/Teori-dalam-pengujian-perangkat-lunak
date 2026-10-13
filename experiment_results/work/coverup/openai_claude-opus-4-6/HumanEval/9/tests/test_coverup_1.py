# file: script_9.py:4-21
# asked: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}
# gained: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}

import pytest

from script_9 import rolling_max


def test_rolling_max_typical_case():
    # Exercises the `running_max is None` branch (first element) and the
    # `else` branch (subsequent elements).
    numbers = [1, 2, 3, 2, 3, 4, 2]
    expected = [1, 2, 3, 3, 3, 4, 4]

    result = rolling_max(numbers)

    assert result == expected
    assert len(result) == len(numbers)
    # Postcondition: each element is the max of the prefix so far.
    for i, value in enumerate(result):
        assert value == max(numbers[: i + 1])


def test_rolling_max_single_element():
    # Only the first-element branch executes; the `else` branch is skipped.
    numbers = [42]
    result = rolling_max(numbers)
    assert result == [42]
    assert result == [max(numbers)]


def test_rolling_max_decreasing():
    # running_max stays the first (largest) element for every iteration.
    numbers = [5, 4, 3, 2, 1]
    result = rolling_max(numbers)
    assert result == [5, 5, 5, 5, 5]
    assert result[0] == numbers[0]


def test_rolling_max_increasing():
    # running_max updates on every iteration.
    numbers = [1, 2, 3, 4, 5]
    result = rolling_max(numbers)
    assert result == [1, 2, 3, 4, 5]


def test_rolling_max_empty_list():
    # Loop body (lines 13-19) is not entered; returns empty result.
    numbers = []
    result = rolling_max(numbers)
    assert result == []


def test_rolling_max_negatives_and_duplicates():
    numbers = [-3, -1, -7, -1, -10]
    result = rolling_max(numbers)
    assert result == [-3, -1, -1, -1, -1]
    for i, value in enumerate(result):
        assert value == max(numbers[: i + 1])


def test_rolling_max_does_not_mutate_input():
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    original = list(numbers)

    result = rolling_max(numbers)

    # The input list must be untouched (no state pollution).
    assert numbers == original
    assert result is not numbers
    assert result == [3, 3, 4, 4, 5, 9, 9, 9]
