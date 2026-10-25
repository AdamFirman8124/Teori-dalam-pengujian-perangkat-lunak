# file: project/f121/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f121 import solution


def test_solution_sums_odd_values_at_even_indices():
    assert solution([1, 2, 3, 4, 5]) == 9


def test_solution_excludes_even_values_and_odd_indices():
    assert solution([2, 1, 4, 3, 6, 5]) == 0


def test_solution_handles_empty_and_negative_values():
    assert solution([]) == 0
    assert solution([-3, 2, -5]) == -8
