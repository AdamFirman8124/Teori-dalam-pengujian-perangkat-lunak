# file: project/f085/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f085 import add


def test_add_sums_even_values_at_odd_indices():
    # Odd indices 1 and 3 hold even values 2 and 4 -> both are counted.
    # Exercises the True branch of the comprehension condition.
    assert add([1, 2, 3, 4]) == 6


def test_add_ignores_odd_values_at_odd_indices():
    # Odd indices 1 and 3 hold odd values 1 and 3 -> nothing is counted.
    # Exercises the False branch of the comprehension condition.
    assert add([0, 1, 0, 3]) == 0


def test_add_empty_list_returns_zero():
    # Exercises the loop body never running (empty range).
    assert add([]) == 0


def test_add_single_element_has_no_odd_indices():
    # range(1, 1, 2) is empty, so the sum is 0.
    assert add([2]) == 0


def test_add_mixed_values_including_negatives():
    # Odd indices 1, 3, 5 hold -2 (even, counted), 7 (odd, skipped), 6 (even, counted).
    assert add([9, -2, 9, 7, 9, 6]) == 4
