# file: script_121.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import pytest
from script_121 import solution


def test_solution_mixed_odd_even_positions():
    """Test with mixed odd and even values at various positions."""
    assert solution([5, 8, 7, 1]) == 12


def test_solution_all_odd_values():
    """Test with all odd values."""
    assert solution([3, 3, 3, 3, 3]) == 9


def test_solution_all_even_values():
    """Test with all even values at even positions."""
    assert solution([30, 13, 24, 321]) == 0


def test_solution_single_odd_element():
    """Test with a single odd element."""
    assert solution([7]) == 7


def test_solution_single_even_element():
    """Test with a single even element."""
    assert solution([8]) == 0


def test_solution_odd_at_even_positions_only():
    """Test with odd values only at even positions."""
    assert solution([1, 2, 3, 4, 5]) == 9


def test_solution_even_at_even_positions_only():
    """Test with even values at even positions."""
    assert solution([2, 1, 4, 3, 6]) == 0


def test_solution_large_list():
    """Test with a larger list."""
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 25
