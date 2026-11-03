# file: project/f121/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f121 import solution


def test_solution_sums_odd_values_at_even_indices():
    # idx 0: value 1 (even index, odd value) -> included
    # idx 1: value 2 (odd index)            -> excluded (first condition False)
    # idx 2: value 3 (even index, odd value) -> included
    # idx 3: value 4 (odd index)            -> excluded (first condition False)
    # idx 4: value 5 (even index, odd value) -> included
    assert solution([1, 2, 3, 4, 5]) == 9


def test_solution_excludes_even_values_at_even_indices():
    # idx 0: value 2 (even index, even value) -> excluded (second condition False)
    # idx 2: value 4 (even index, even value) -> excluded (second condition False)
    assert solution([2, 1, 4, 3]) == 0


def test_solution_empty_list_returns_zero():
    assert solution([]) == 0


def test_solution_single_odd_element():
    assert solution([7]) == 7


def test_solution_single_even_element():
    assert solution([8]) == 0


def test_solution_all_odd_values():
    # Only indices 0 and 2 hold odd values; index 1 is skipped.
    assert solution([1, 3, 5]) == 6


def test_solution_negative_odd_values():
    # In Python, -3 % 2 == 1, so negative odd values at even indices count.
    assert solution([-3, 2, -5]) == -8
