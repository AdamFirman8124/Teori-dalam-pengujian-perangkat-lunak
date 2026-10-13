# file: script_9.py:4-21
# asked: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}
# gained: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}

import script_9


def test_rolling_max_empty_list():
    assert script_9.rolling_max([]) == []


def test_rolling_max_tracks_initial_and_subsequent_maxima():
    numbers = [1, 2, 3, 2, 3, 4, 2]

    assert script_9.rolling_max(numbers) == [1, 2, 3, 3, 3, 4, 4]
