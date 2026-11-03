# file: project/f109/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}

import pytest

from f109 import move_one_ball


def test_move_one_ball_empty_returns_true():
    """Covers lines 3-4: empty array short-circuits to True."""
    assert move_one_ball([]) is True


def test_move_one_ball_single_element_returns_true():
    """Covers lines 5-10 with a single-element array (min_index == 0)."""
    assert move_one_ball([7]) is True


def test_move_one_ball_already_sorted_returns_true():
    """Covers lines 5-11 and 14 with min_index == 0 (no rotation needed)."""
    assert move_one_ball([1, 2, 3, 4]) is True


def test_move_one_ball_rotated_returns_true():
    """Covers lines 5-11 and 14 with min_index > 0 (valid rotation)."""
    assert move_one_ball([3, 4, 5, 1, 2]) is True


def test_move_one_ball_unrotatable_returns_false():
    """Covers lines 12-13: mismatch found during comparison -> False."""
    assert move_one_ball([1, 3, 2]) is False


def test_move_one_ball_rotated_unrotatable_returns_false():
    """Covers lines 12-13 with a rotated array that cannot be sorted."""
    assert move_one_ball([2, 3, 4, 1, 5]) is False


def test_move_one_ball_duplicates_rotated_returns_true():
    """Duplicate minimum values still rotate into sorted order -> True."""
    assert move_one_ball([2, 3, 1, 1, 2]) is True


def test_move_one_ball_pure_function_no_state_pollution():
    """The function must not mutate its input (no side effects)."""
    arr = [3, 4, 5, 1, 2]
    original = list(arr)
    result = move_one_ball(arr)
    assert result is True
    assert arr == original
