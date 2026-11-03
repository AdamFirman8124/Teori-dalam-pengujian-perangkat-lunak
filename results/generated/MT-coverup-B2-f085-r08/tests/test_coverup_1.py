# file: project/f085/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f085 import add


def test_add_empty_list_loop_never_runs():
    """Empty list -> range(1, 0, 2) is empty, so the comprehension loop
    body (and its condition) never executes; sum of nothing is 0."""
    assert add([]) == 0


def test_add_single_element_loop_never_runs():
    """Single-element list -> range(1, 1, 2) is empty, loop body skipped."""
    assert add([7]) == 0


def test_add_sums_even_values_at_odd_indices():
    """Even values at odd indices satisfy the condition and are summed
    (covers the True branch of the comprehension's if)."""
    assert add([1, 2, 3, 4]) == 6  # lst[1] == 2 and lst[3] == 4


def test_add_skips_odd_values_at_odd_indices():
    """Odd values at odd indices fail the condition and are filtered out
    (covers the False branch of the comprehension's if)."""
    assert add([1, 1, 3, 3]) == 0


def test_add_mixed_values():
    """Mixed input: only even values located at odd indices contribute."""
    assert add([0, 1, 2, 4, 5, 6]) == 10  # lst[1]=1 (odd, skipped), lst[3]=4, lst[5]=6
