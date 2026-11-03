# file: project/f109/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}

import pytest

from f109 import move_one_ball


def test_move_one_ball_empty_returns_true():
    """Covers lines 3-4: empty input short-circuits to True."""
    assert move_one_ball([]) is True


def test_move_one_ball_single_element_returns_true():
    """Covers lines 5-11 and 14: single element is trivially sortable."""
    assert move_one_ball([7]) is True


def test_move_one_ball_already_sorted_returns_true():
    """Covers lines 5-11 and 14 with min_index == 0 (rotation is a no-op)."""
    assert move_one_ball([1, 2, 3, 4, 5]) is True


def test_move_one_ball_rotated_returns_true():
    """Covers lines 5-11 and 14 with min_index > 0 (real rotation)."""
    assert move_one_ball([3, 4, 5, 1, 2]) is True


def test_move_one_ball_unsortable_returns_false():
    """Covers lines 12-13: mismatch found inside the loop returns False."""
    assert move_one_ball([1, 3, 2]) is False


def test_move_one_ball_rotated_unsortable_returns_false():
    """Covers lines 12-13 with a rotated array that cannot be sorted."""
    assert move_one_ball([2, 3, 4, 1, 5]) is False


def test_move_one_ball_duplicates_rotated_returns_true():
    """Covers lines 5-11 and 14 with duplicate minimum values."""
    assert move_one_ball([2, 3, 1, 1]) is True


def test_move_one_ball_pure_function_no_state_pollution():
    """Verifies the function does not mutate its input (no side effects)."""
    arr = [3, 4, 5, 1, 2]
    original = list(arr)
    result = move_one_ball(arr)
    assert result is True
    assert arr == original
