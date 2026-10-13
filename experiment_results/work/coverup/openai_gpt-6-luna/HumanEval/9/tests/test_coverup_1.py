# file: script_9.py:4-21
# asked: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}
# gained: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}

import script_9


def test_rolling_max_with_values_updates_and_retains_running_maximum():
    numbers = [1, 2, 3, 2, 3, 4, 2]

    result = script_9.rolling_max(numbers)

    assert result == [1, 2, 3, 3, 3, 4, 4]


def test_rolling_max_with_empty_list_returns_empty_list():
    assert script_9.rolling_max([]) == []
