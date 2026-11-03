# file: project/f109/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}

import pytest

from f109 import move_one_ball


def test_move_one_ball_empty_array():
    """Lines 3-4: empty array should return True immediately."""
    assert move_one_ball([]) is True


def test_move_one_ball_single_element():
    """Single element is trivially a sorted rotation (lines 5-14)."""
    assert move_one_ball([7]) is True


def test_move_one_ball_already_sorted():
    """An already sorted array is a rotation of itself with min at index 0."""
    assert move_one_ball([1, 2, 3, 4, 5]) is True


def test_move_one_ball_rotatable_true():
    """A rotation of the sorted array must return True (lines 5-12, 14)."""
    # sorted is [1, 2, 3, 4, 5]; [3, 4, 5, 1, 2] is that rotation
    assert move_one_ball([3, 4, 5, 1, 2]) is True


def test_move_one_ball_rotatable_false():
    """An array that is not any rotation of its sorted version returns False (line 13)."""
    assert move_one_ball([3, 5, 4, 1, 2]) is False


def test_move_one_ball_duplicates_min_at_end():
    """Duplicates of the minimum: rotation chosen from the first min index still works."""
    assert move_one_ball([2, 3, 4, 1, 1]) is True


def test_move_one_ball_duplicates_not_rotatable():
    """With duplicates, a non-rotatable arrangement must return False."""
    assert move_one_ball([2, 1, 3, 1]) is False


def test_move_one_ball_negative_numbers():
    """Works with negative values; min is negative."""
    # sorted is [-5, -4, -2, -1, 3]; [-2, -1, 3, -5, -4] is that rotation
    assert move_one_ball([-2, -1, 3, -5, -4]) is True
    # sorted is [-5, -4, -2, -1, 4]; rotating at first min (-5) yields
    # [-5, -2, -1, 4, -4], which differs from sorted at index 1 -> False
    assert move_one_ball([-2, -1, 4, -4, -5]) is False


def test_move_one_ball_does_not_mutate_input():
    """Postcondition: the input list must not be modified (no state pollution)."""
    arr = [3, 4, 5, 1, 2]
    original = list(arr)
    result = move_one_ball(arr)
    assert result is True
    assert arr == original
