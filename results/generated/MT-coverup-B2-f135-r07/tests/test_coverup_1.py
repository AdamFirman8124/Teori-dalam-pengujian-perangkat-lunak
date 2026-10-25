# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

from f135 import can_arrange


def test_can_arrange_returns_minus_one_without_decrease():
    assert can_arrange([]) == -1
    assert can_arrange([1]) == -1
    assert can_arrange([1, 2, 3]) == -1


def test_can_arrange_returns_last_decreasing_index():
    assert can_arrange([1, 3, 2, 5, 4]) == 4
    assert can_arrange([3, 2, 1]) == 2
