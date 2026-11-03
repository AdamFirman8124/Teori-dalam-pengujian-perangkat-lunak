

# Generated at 2026-11-03 04:30:34.159255
# Unit test for function solution
def test_solution():import pytest


def test_solution_basic():
    """Example: odd values at even indices 0 and 2."""
    assert module_0.solution([1, 2, 3]) == 4


def test_solution_empty_list():
    """Empty list should return 0."""
    assert module_0.solution([]) == 0


def test_solution_no_odd_at_even_indices():
    """All values even, nothing to sum."""
    assert module_0.solution([2, 4, 6, 8]) == 0


def test_solution_all_odd_values():
    """Odd values at even indices 0 and 2 count; index 1 is skipped."""
    assert module_0.solution([1, 1, 1]) == 2


def test_solution_mixed_values():
    """5 and 7 at even indices, 8 and 1 skipped."""
    assert module_0.solution([5, 8, 7, 1]) == 12


def test_solution_single_odd_element():
    """Single element at index 0 with odd value."""
    assert module_0.solution([3]) == 3


def test_solution_single_even_element():
    """Single element at index 0 with even value."""
    assert module_0.solution([2]) == 0


def test_solution_odd_at_odd_index_ignored():
    """Odd values at odd indices should not be counted."""
    assert module_0.solution([2, 3, 4, 5]) == 0


def test_solution_negative_numbers():
    """Negative odd values at even indices are counted."""
    assert module_0.solution([-3, 2, -5]) == -8


def test_solution_longer_list():
    """Indices 0 (1), 2 (3), 4 (5) -> sum 9; index 6 value 6 skipped."""
    assert module_0.solution([1, 2, 3, 4, 5, 6, 6]) == 9


def test_solution_zero_not_counted():
    """Zero is even, should not be included even at even index."""
    assert module_0.solution([0, 1, 0, 1]) == 0

# Generated at 2026-11-03 04:34:01.322262
# Unit test for function solution
def test_solution():
    # Empty list should return 0
    assert module_0.solution([]) == 0

    # No odd elements at even indices
    assert module_0.solution([2, 3, 4, 5]) == 0

    # Odd element only at odd index (should not count)
    assert module_0.solution([0, 1]) == 0

    # Basic case: odd elements at even indices
    assert module_0.solution([5, 8, 6, 4]) == 5

    # Multiple qualifying elements
    assert module_0.solution([1, 2, 3]) == 4

    # All elements are 1 at even indices
    assert module_0.solution([1, 1, 1, 1]) == 2

    # Longer list with mixed values
    assert module_0.solution([3, 3, 3, 3, 3, 3]) == 9

    # Negative odd numbers at even indices count (Python: -3 % 2 == 1)
    assert module_0.solution([-3, 5, -7, 8]) == -10

    # Even-index odd values combined with even-index even values
    assert module_0.solution([7, 2, 4, 1, 9, 6]) == 16

    # Single qualifying element
    assert module_0.solution([1]) == 1

    # Single non-qualifying element
    assert module_0.solution([2]) == 0

# Generated at 2026-11-03 04:37:21.410642
# Unit test for function solution
def test_solution():
    # Test with empty list
    assert module_0.solution([]) == 0

    # Test with example cases
    assert module_0.solution([3, 3, 3, 3, 3]) == 9
    assert module_0.solution([3, 2, 3, 2, 3]) == 9

    # Test with mixed values - only odd values at even indices count
    assert module_0.solution([1, 2, 3, 4]) == 4
    assert module_0.solution([2, 3, 4, 5, 6, 7]) == 0

    # Test with even values at even indices (should not be counted)
    assert module_0.solution([2, 1, 4, 3, 6, 5]) == 0

    # Test with single element list
    assert module_0.solution([1]) == 1
    assert module_0.solution([2]) == 0

    # Test with negative odd numbers
    assert module_0.solution([-1, 2, -3, 4]) == -4
    assert module_0.solution([-1, -1, -1]) == -2

    # Test with all even numbers
    assert module_0.solution([2, 4, 6, 8]) == 0

    # Test with odd values only at odd indices
    assert module_0.solution([2, 1, 4, 3]) == 0

    # Test with larger list
    assert module_0.solution(list(range(10))) == 1 + 3 + 5 + 7 + 9  # 25

    # Test with zeros
    assert module_0.solution([0, 0, 0]) == 0

    # Test with large numbers
    assert module_0.solution([999999, 2, 999999]) == 1999998