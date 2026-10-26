# file: project/f121/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f121 import solution


def test_solution_empty_list_executes_return_line():
    assert solution([]) == 0


def test_solution_sums_odd_values_at_even_indices():
    # idx 0 -> 1 (odd, counted), idx 1 -> 2 (odd index, skipped),
    # idx 2 -> 3 (odd, counted), idx 3 -> 4 (odd index, skipped)
    assert solution([1, 2, 3, 4]) == 4


def test_solution_skips_even_values_at_even_indices():
    # idx 0 -> 2 (even, skipped), idx 2 -> 4 (even, skipped)
    assert solution([2, 1, 4, 3]) == 0


def test_solution_single_element_odd():
    assert solution([7]) == 7


def test_solution_single_element_even():
    assert solution([8]) == 0


def test_solution_does_not_mutate_input():
    lst = [1, 2, 3, 4]
    original = list(lst)
    solution(lst)
    assert lst == original


def test_solution_negative_odd_values():
    # -3 is odd in Python (-3 % 2 == 1), at even index 0
    assert solution([-3, 5, -7]) == -10
