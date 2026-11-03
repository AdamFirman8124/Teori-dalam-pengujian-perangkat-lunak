# file: project/f085/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f085 import add


def test_add_empty_list():
    """Empty list: range(1, 0, 2) is empty, so the comprehension body never
    runs and the result is 0. Executes line 3 with zero iterations."""
    assert add([]) == 0


def test_add_even_values_at_odd_indices():
    """Even values at odd indices are summed (condition True branch)."""
    # Odd indices are 1 and 3; lst[1] == 2 and lst[3] == 4 are both even.
    assert add([1, 2, 3, 4]) == 6


def test_add_odd_values_at_odd_indices():
    """Odd values at odd indices are skipped (condition False branch)."""
    # Odd indices are 1 and 3; lst[1] == 3 and lst[3] == 7 are both odd.
    assert add([1, 3, 5, 7]) == 0


def test_add_mixed_values_both_branches():
    """Mixed values exercise both branches of the parity condition."""
    # Odd indices are 1, 3, 5; lst[1] == 2 (even, kept),
    # lst[3] == 5 (odd, skipped), lst[5] == 6 (even, kept).
    assert add([1, 2, 3, 5, 7, 6]) == 8


def test_add_single_element_list():
    """A single-element list has no odd indices, so the result is 0."""
    assert add([4]) == 0
