# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

import pytest

from f135 import can_arrange


def test_can_arrange_empty_list_skips_loop():
    assert can_arrange([]) == -1


def test_can_arrange_single_element_skips_loop():
    assert can_arrange([5]) == -1


def test_can_arrange_sorted_ascending_returns_minus_one():
    assert can_arrange([1, 2, 3, 4]) == -1


def test_can_arrange_sorted_with_equal_neighbours_returns_minus_one():
    assert can_arrange([2, 2, 2]) == -1


def test_can_arrange_single_descent_returns_its_index():
    assert can_arrange([1, 3, 2]) == 2


def test_can_arrange_descent_at_first_pair():
    assert can_arrange([5, 4, 6, 7]) == 1


def test_can_arrange_multiple_descents_returns_last_index():
    assert can_arrange([3, 1, 2, 0]) == 3


def test_can_arrange_fully_descending_returns_last_index():
    assert can_arrange([9, 8, 7, 6]) == 3


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([], -1),
        ([1], -1),
        ([1, 2, 3], -1),
        ([2, 1], 1),
        ([1, 2, 1, 2, 1], 4),
        ([0, -1, -2], 2),
    ],
)
def test_can_arrange_parametrized(arr, expected):
    original = list(arr)
    result = can_arrange(arr)
    assert result == expected
    assert arr == original, "can_arrange must not mutate its input"
