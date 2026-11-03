# file: project/f085/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f085 import add


def test_add_all_even_at_odd_indices():
    # Odd indices 1 and 3 hold even values 2 and 4 -> both included
    assert add([1, 2, 3, 4]) == 6


def test_add_all_odd_at_odd_indices():
    # Odd indices 1 and 3 hold odd values 3 and 7 -> both filtered out
    assert add([1, 3, 5, 7]) == 0


def test_add_mixed_parity():
    # Odd indices 1, 3, 5 hold 2, 4, 6 -> all even, sum = 12
    assert add([1, 2, 3, 4, 5, 6]) == 12


def test_add_empty_list():
    # range(1, 0, 2) is empty -> comprehension body never runs, sum is 0
    assert add([]) == 0


def test_add_single_element():
    # range(1, 1, 2) is empty -> sum is 0
    assert add([1]) == 0


def test_add_negative_even_at_odd_index():
    # Negative even number at an odd index is included
    assert add([1, -2, 3, 4]) == 2
