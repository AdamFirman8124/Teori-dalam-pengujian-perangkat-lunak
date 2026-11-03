# file: project/f121/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f121 import solution


def test_empty_list_returns_zero():
    """Covers the case where the comprehension body never executes."""
    assert solution([]) == 0


def test_odd_number_at_even_index_is_included():
    """idx%2==0 True and x%2==1 True: element contributes to the sum."""
    assert solution([1]) == 1


def test_even_number_at_even_index_is_excluded():
    """idx%2==0 True but x%2==1 False: element is filtered out."""
    assert solution([2]) == 0


def test_odd_number_at_odd_index_is_excluded():
    """idx%2==0 False: short-circuits before evaluating x%2==1."""
    assert solution([0, 1]) == 0


def test_mixed_list():
    """Exercises every branch combination of the comprehension condition."""
    # idx 0: 3 (odd, even index) -> included
    # idx 1: 2 (odd index)       -> excluded
    # idx 2: 4 (even value)      -> excluded
    # idx 3: 7 (odd index)       -> excluded
    # idx 4: 5 (odd, even index) -> included
    assert solution([3, 2, 4, 7, 5]) == 8


def test_all_even_values_at_even_indices():
    """Every even-index element is even, so nothing is summed."""
    assert solution([2, 1, 4, 3, 6, 5]) == 0


def test_negative_odd_numbers_at_even_indices():
    """Python's % makes negative odds satisfy x % 2 == 1 (e.g. -3 % 2 == 1)."""
    assert solution([-3, 2, -5]) == -8
