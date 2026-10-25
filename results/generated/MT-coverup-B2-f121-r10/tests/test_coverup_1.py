# file: project/f121/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f121 import solution


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([], 0),
        ([1], 1),
        ([2], 0),
        ([1, 2, 3, 4], 4),
        ([4, 3, 2, 1], 0),
        ([1, 100, 3, 200, 5], 9),
        ([2, 1, 4, 3], 0),
        ([0, 7, 0, 9], 0),
        ([-1, 2, -3], -4),
    ],
)
def test_solution_returns_sum_of_odd_values_at_even_indices(lst, expected):
    original = list(lst)
    result = solution(lst)
    assert result == expected
    assert lst == original, "solution must not mutate its input"


def test_solution_ignores_odd_values_at_odd_indices():
    assert solution([2, 1, 2, 3, 2, 5]) == 0


def test_solution_accepts_tuple_input():
    assert solution((1, 2, 3, 4, 5)) == 9


def test_solution_returns_int_zero_for_empty_input():
    result = solution([])
    assert result == 0
    assert isinstance(result, int)
