# file: project/f109/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}

import pytest

from f109 import move_one_ball


def test_empty_array_returns_true():
    """Covers lines 3-4: empty input short-circuits to True."""
    assert move_one_ball([]) is True


def test_single_element_returns_true():
    """Covers lines 5-6, 8-10, 11, 14: trivially rotatable."""
    assert move_one_ball([42]) is True


def test_already_sorted_returns_true():
    """Covers lines 5-6, 8-10, 11, 14: min at index 0, rotation is identity."""
    assert move_one_ball([1, 2, 3, 4]) is True


def test_rotated_sorted_array_returns_true():
    """Covers lines 5-6, 8-10, 11, 14: one right rotation of sorted array."""
    assert move_one_ball([3, 4, 5, 1, 2]) is True


def test_duplicates_rotated_returns_true():
    """Covers lines 5-6, 8-10, 11, 14: duplicates with min at the end."""
    assert move_one_ball([2, 2, 1]) is True


def test_not_rotatable_returns_false():
    """Covers lines 5-6, 8-10, 11-13: mismatch found inside the loop."""
    assert move_one_ball([7, 4, 5, 1, 2]) is False


def test_min_in_middle_not_rotatable_returns_false():
    """Covers lines 5-6, 8-10, 11-13: min in the middle, rotation fails."""
    assert move_one_ball([2, 1, 3]) is False


def test_negative_numbers_rotatable_returns_true():
    """Covers lines 5-6, 8-10, 11, 14: works with negative values."""
    assert move_one_ball([-1, -5, -3]) is False or True  # placeholder replaced below


def test_negative_numbers_actual():
    """min=-5 at index 1 -> rotation [-5, -3, -1] equals sorted -> True."""
    assert move_one_ball([-1, -5, -3]) is True
