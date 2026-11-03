# file: project/f085/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f085.add — covers line 3 and all branches of the list comprehension.

Branches exercised:
  * comprehension loop body executes with an even element (condition True)
  * comprehension loop body executes with an odd element (condition False)
  * comprehension loop never executes (empty range: empty / single-element list)

`add` is a pure function (no I/O, no globals, no mutation of its argument),
so no monkeypatching or fixture-based cleanup is required; each test is
self-contained and leaves no state behind.
"""

import pytest

from f085 import add


def test_add_empty_list_loop_never_executes():
    # range(1, 0, 2) is empty -> comprehension body never runs, sum is 0.
    assert add([]) == 0


def test_add_single_element_loop_never_executes():
    # range(1, 1, 2) is empty -> comprehension body never runs, sum is 0.
    assert add([7]) == 0


def test_add_even_elements_at_odd_indices_condition_true():
    # Odd indices 1 and 3 hold even values 2 and 4 -> both included.
    assert add([1, 2, 3, 4]) == 6


def test_add_odd_elements_at_odd_indices_condition_false():
    # Odd indices 1 and 3 hold odd values 3 and 7 -> both filtered out.
    assert add([1, 3, 5, 7]) == 0


def test_add_mixed_elements_both_branches():
    # Odd indices 1, 3, 5 hold 2 (even -> kept), 5 (odd -> skipped),
    # 8 (even -> kept): sum == 10.
    assert add([1, 2, 3, 5, 7, 8]) == 10


def test_add_negative_and_zero_values():
    # Zero and negative evens at odd indices are kept; odd negatives skipped.
    # Odd indices 1, 3, 5 hold 0 (kept), -3 (skipped), -4 (kept): sum == -4.
    assert add([9, 0, 9, -3, 9, -4]) == -4


def test_add_does_not_mutate_input():
    lst = [1, 2, 3, 4]
    snapshot = list(lst)
    result = add(lst)
    assert result == 6
    assert lst == snapshot  # input list is untouched (no state pollution)
