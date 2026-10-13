# file: script_9.py:4-21
# asked: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}
# gained: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}

import pytest

from script_9 import rolling_max


def test_rolling_max_basic():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]


def test_rolling_max_single_element():
    assert rolling_max([5]) == [5]


def test_rolling_max_negative_and_decreasing():
    assert rolling_max([-1, -3, -2, -5]) == [-1, -1, -1, -1]


def test_rolling_max_empty():
    assert rolling_max([]) == []


def test_rolling_max_equals():
    assert rolling_max([2, 2, 1, 2]) == [2, 2, 2, 2]


def test_rolling_max_does_not_mutate_input():
    numbers = [3, 1, 2]
    copy = list(numbers)
    rolling_max(numbers)
    assert numbers == copy
