# file: project/f085/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f085 import add


def test_add_sums_even_values_at_odd_indices():
    # Indices 1 and 3 hold 2 and 4 (both even) -> 2 + 4 = 6
    # Covers line 3, the comprehension loop, and the True branch of the filter.
    assert add([1, 2, 3, 4]) == 6


def test_add_skips_odd_values_at_odd_indices():
    # Indices 1 and 3 hold 3 and 7 (both odd) -> nothing is summed.
    # Covers the False branch of the filter condition.
    assert add([1, 3, 5, 7]) == 0


def test_add_mixed_values_at_odd_indices():
    # Index 1 -> 4 (even, counted), index 3 -> 5 (odd, skipped),
    # index 5 -> 6 (even, counted) -> 4 + 6 = 10
    assert add([0, 4, 0, 5, 0, 6]) == 10


def test_add_empty_list():
    # Empty list -> range(1, 0, 2) is empty, loop body never runs.
    assert add([]) == 0


def test_add_single_element_list():
    # range(1, 1, 2) is empty -> loop body never runs.
    assert add([42]) == 0


def test_add_negative_even_values_at_odd_indices():
    # Negative even values at odd indices are counted: -2 + 4 = 2
    assert add([1, -2, 3, 4]) == 2
