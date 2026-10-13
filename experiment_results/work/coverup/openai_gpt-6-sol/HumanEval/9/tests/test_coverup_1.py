# file: script_9.py:4-21
# asked: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}
# gained: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}

from script_9 import rolling_max


def test_rolling_max_with_empty_list():
    assert rolling_max([]) == []


def test_rolling_max_with_increasing_and_decreasing_values():
    numbers = [1, 2, 3, 2, 3, 4, 2]

    assert rolling_max(numbers) == [1, 2, 3, 3, 3, 4, 4]
