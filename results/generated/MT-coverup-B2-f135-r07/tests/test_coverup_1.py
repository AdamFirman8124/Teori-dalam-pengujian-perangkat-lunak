# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

"""Tests for f135.can_arrange.

can_arrange returns the largest index i (>= 1) such that arr[i] < arr[i-1],
or -1 if the array is non-decreasing (or has fewer than two elements).
"""

import pytest

from f135 import can_arrange


def test_empty_list_loop_never_runs():
    # len(arr) == 0 -> while-condition is False immediately.
    # Covers lines 3, 4 and 9 (and the False branch of the while).
    assert can_arrange([]) == -1


def test_single_element_loop_never_runs():
    # i starts at 1, so with one element the loop body never executes.
    assert can_arrange([42]) == -1


def test_sorted_array_condition_never_true():
    # Loop runs (lines 5, 6, 8 executed) but the if-body (line 7) is skipped,
    # exercising the False branch of the if.
    assert can_arrange([1, 2, 3, 4, 5]) == -1


def test_single_descent_returns_its_index():
    # Only descent is at i == 3 (3 < 4), covering the True branch of the if.
    assert can_arrange([1, 2, 4, 3]) == 3


def test_multiple_descents_returns_last_index():
    # Descents at i == 1, 2 and 3; the final assignment (line 7) must win.
    assert can_arrange([5, 4, 3, 2]) == 3


def test_mixed_array_returns_last_descent_index():
    # Descents at i == 2 (2 < 3) and i == 4 (0 < 4); interleaved True/False
    # branches of the if inside the loop.
    assert can_arrange([1, 3, 2, 4, 0]) == 4


def test_equal_neighbors_are_not_descents():
    # Comparison is strict '<', so equal adjacent values leave ind at -1.
    assert can_arrange([1, 1, 2, 2]) == -1


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([], -1),
        ([7], -1),
        ([1, 2], -1),
        ([2, 1], 1),
        ([1, 3, 2, 5, 4, 6], 4),
        ([10, 20, 30, 25, 40, 35, 50], 5),
    ],
)
def test_can_arrange_parametrized(arr, expected):
    assert can_arrange(arr) == expected
