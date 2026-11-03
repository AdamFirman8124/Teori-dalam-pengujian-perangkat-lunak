# file: project/f085/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f085 import add


def test_add_empty_list():
    """Empty list: no odd indices exist, sum is 0 (covers loop-not-taken branch)."""
    assert add([]) == 0


def test_add_single_element():
    """Single element: range(1, 1, 2) is empty, sum is 0."""
    assert add([7]) == 0


def test_add_even_elements_at_odd_indices():
    """Elements at odd indices that are even are summed (condition true branch)."""
    assert add([1, 2, 3, 4]) == 6  # indices 1 and 3 -> 2 + 4


def test_add_odd_elements_at_odd_indices():
    """Elements at odd indices that are odd are skipped (condition false branch)."""
    assert add([0, 1, 0, 3]) == 0  # indices 1 and 3 -> 1 and 3, both odd


def test_add_mixed_elements():
    """Mixed case: only even values at odd indices contribute to the sum."""
    assert add([5, 2, 7, 3, 9, 8]) == 10  # indices 1, 3, 5 -> 2 + 3 + 8


def test_add_negative_even_elements():
    """Negative even numbers at odd indices are included (n % 2 == 0 holds)."""
    assert add([1, -2, 3, -4]) == -6  # indices 1 and 3 -> -2 + -4
