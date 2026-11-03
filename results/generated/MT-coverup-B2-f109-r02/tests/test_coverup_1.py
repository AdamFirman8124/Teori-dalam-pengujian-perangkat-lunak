# file: project/f109/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}

"""Tests for f109.move_one_ball.

Covers all previously unexecuted lines 3-14 and both branches of the
mismatch check (line 12 -> line 13 early return, and loop fall-through
to line 14).

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching/teardown is required; each test also asserts the
input list is left unmodified to guard against state pollution.
"""

import pytest

from f109 import move_one_ball


def test_empty_array_returns_true():
    """Lines 3-4: an empty array is trivially 'sorted' -> True."""
    arr = []
    assert move_one_ball(arr) is True
    assert arr == []  # input untouched


def test_single_element_returns_true():
    """Covers non-empty path with a one-iteration loop -> line 14."""
    arr = [42]
    assert move_one_ball(arr) is True
    assert arr == [42]


def test_already_sorted_returns_true():
    """min_index == 0, rotation is a no-op; loop matches everywhere."""
    arr = [1, 2, 3, 4]
    assert move_one_ball(arr) is True
    assert arr == [1, 2, 3, 4]


def test_rotated_sorted_array_returns_true():
    """Lines 5-11 plus line 12 False-branch and line 14: a right-rotation
    of a sorted array is detected as sortable."""
    arr = [3, 4, 5, 1, 2]
    assert move_one_ball(arr) is True
    assert arr == [3, 4, 5, 1, 2]


def test_mismatch_returns_false_early():
    """Line 12 True-branch and line 13: rotation at the first minimum
    does not yield the sorted order -> False returned inside the loop."""
    arr = [3, 5, 4, 1, 2]
    assert move_one_ball(arr) is False
    assert arr == [3, 5, 4, 1, 2]


def test_unsortable_array_returns_false():
    """Another False case exercising the mismatch branch."""
    arr = [2, 1, 4, 3]
    assert move_one_ball(arr) is False
    assert arr == [2, 1, 4, 3]


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([], True),                 # empty -> early True
        ([7], True),                # single element
        ([1, 2], True),             # already sorted
        ([2, 1], True),             # one rotation fixes it
        ([1, 3, 2], False),         # rotation at min index can't sort it
        ([3, 4, 5, 1, 2], True),    # classic rotated-sorted case
        ([2, 3, 4, 5, 1], True),    # min at last position
        ([5, 1, 2, 3, 4], True),    # min at first position
        ([3, 5, 4, 1, 2], False),   # mismatch inside loop
    ],
)
def test_move_one_ball_parametrized(arr, expected):
    assert move_one_ball(arr) is expected
