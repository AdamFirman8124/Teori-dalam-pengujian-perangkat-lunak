# file: project/f121/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f121 import solution


def test_solution_empty_list():
    """Empty input: the comprehension body (line 3) still executes and yields 0."""
    assert solution([]) == 0


def test_solution_mixed_indices_and_values():
    """Only elements at even indices that are odd values are summed."""
    # idx 0: 1 (even idx, odd val -> included), idx 1: 2 (skipped),
    # idx 2: 3 (even idx, odd val -> included), idx 3: 4 (skipped),
    # idx 4: 5 (even idx, odd val -> included)
    assert solution([1, 2, 3, 4, 5]) == 1 + 3 + 5


def test_solution_no_matches():
    """Even-indexed elements that are even values are all filtered out."""
    assert solution([2, 1, 4, 3, 6, 5]) == 0


def test_solution_odd_indexed_odd_values_excluded():
    """Odd values at odd indices must not be counted."""
    # Odd values only at odd indices -> sum is 0
    assert solution([2, 1, 4, 3]) == 0


def test_solution_negative_numbers():
    """Python's modulo makes negative odd numbers satisfy x % 2 == 1."""
    # idx 0: -1 (odd), idx 2: -3 (odd) -> -1 + -3 = -4
    assert solution([-1, 2, -3, 4]) == -4


def test_solution_zero_at_even_index():
    """Zero at an even index is even, so it is excluded."""
    assert solution([0, 1, 2, 3]) == 0


def test_solution_single_element():
    """Single odd element at index 0 is included."""
    assert solution([7]) == 7
    assert solution([8]) == 0


def test_solution_returns_int():
    """The result is an int (sum of ints)."""
    result = solution([1, 2, 3])
    assert isinstance(result, int)
    assert result == 4
