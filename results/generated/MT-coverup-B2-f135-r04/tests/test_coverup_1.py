# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

from f135 import can_arrange


def test_can_arrange_returns_minus_one_when_already_arranged():
    arr = [1, 2, 2, 4]
    original = arr.copy()

    assert can_arrange(arr) == -1
    assert arr == original


def test_can_arrange_returns_last_decreasing_index():
    arr = [4, 2, 3, 1, 5]
    original = arr.copy()

    assert can_arrange(arr) == 3
    assert arr == original


def test_can_arrange_handles_empty_list():
    arr = []

    assert can_arrange(arr) == -1
    assert arr == []
