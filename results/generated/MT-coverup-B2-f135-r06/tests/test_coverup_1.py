# file: project/f135/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 7], [6, 8]]}

"""Tests for f135.can_arrange.

can_arrange returns the largest index i (>= 1) such that arr[i] < arr[i-1],
or -1 if no such index exists (including for arrays of length 0 or 1,
where the while-loop body never runs).

The function is pure (no I/O, no globals, no mutable state), so no
monkeypatching or teardown is required; each test operates only on local
data, avoiding any state pollution.
"""

import pytest

from f135 import can_arrange


def test_empty_array_loop_never_runs():
    """len(arr) == 0: the while condition is False immediately (line 5 branch)."""
    assert can_arrange([]) == -1


def test_single_element_loop_never_runs():
    """len(arr) == 1: the while condition is False immediately (line 5 branch)."""
    assert can_arrange([7]) == -1


def test_non_decreasing_array_if_never_true():
    """Loop body runs but the if-condition (line 6) is never True -> ind stays -1."""
    assert can_arrange([1, 2, 3]) == -1


def test_equal_elements_if_never_true():
    """Strict '<' means equal neighbours do not count as a descent."""
    assert can_arrange([2, 2, 2]) == -1


def test_single_descent_if_true():
    """The if-condition (line 6) is True once, so line 7 executes."""
    assert can_arrange([1, 2, 4, 3, 5]) == 3


def test_strictly_decreasing_returns_last_index():
    """Every iteration takes the True branch; the last index wins."""
    assert can_arrange([5, 4, 3, 2, 1]) == 4


def test_multiple_descents_returns_largest_index():
    """ind is overwritten on each descent, so the largest index is returned."""
    assert can_arrange([3, 1, 4, 1, 5, 9, 2, 6]) == 6


def test_descent_at_first_possible_index_only():
    """A descent only at i == 1 still exercises the True branch."""
    assert can_arrange([10, 1, 2, 3]) == 1


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([], -1),
        ([1], -1),
        ([1, 2, 3], -1),
        ([1, 2, 4, 3, 5], 3),
        ([5, 4, 3, 2, 1], 4),
        ([3, 1, 4, 1, 5, 9, 2, 6], 6),
    ],
)
def test_can_arrange_parametrized(arr, expected):
    """Parametrized sweep over all branches of the function."""
    assert can_arrange(arr) == expected
