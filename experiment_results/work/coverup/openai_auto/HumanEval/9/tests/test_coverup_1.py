# file: script_9.py:4-21
# asked: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}
# gained: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}

from script_9 import rolling_max


def test_rolling_max_empty_list():
    assert rolling_max([]) == []


def test_rolling_max_tracks_increases_and_decreases():
    numbers = [1, 2, 3, 2, 3, 4, 2]

    result = rolling_max(numbers)

    assert result == [1, 2, 3, 3, 3, 4, 4]
    assert numbers == [1, 2, 3, 2, 3, 4, 2]
