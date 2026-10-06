# file: script_109.py:1-39
# asked: {"lines": [28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39], "branches": [[28, 29], [28, 30], [36, 37], [36, 39], [37, 36], [37, 38]]}
# gained: {"lines": [28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39], "branches": [[28, 29], [28, 30], [36, 37], [36, 39], [37, 36], [37, 38]]}

import pytest
from script_109 import move_one_ball


def test_move_one_ball_empty_array():
    """Test with empty array - should return True"""
    assert move_one_ball([]) == True


def test_move_one_ball_single_element():
    """Test with single element - should return True"""
    assert move_one_ball([5]) == True


def test_move_one_ball_already_sorted():
    """Test with already sorted array - should return True"""
    assert move_one_ball([1, 2, 3, 4, 5]) == True


def test_move_one_ball_rotated_sorted():
    """Test with rotated sorted array - should return True"""
    assert move_one_ball([3, 4, 5, 1, 2]) == True


def test_move_one_ball_not_sortable():
    """Test with array that cannot be sorted by rotation - should return False"""
    assert move_one_ball([3, 5, 4, 1, 2]) == False


def test_move_one_ball_reverse_sorted():
    """Test with reverse sorted array - should return False"""
    assert move_one_ball([5, 4, 3, 2, 1]) == False


def test_move_one_ball_two_elements_sorted():
    """Test with two elements in sorted order - should return True"""
    assert move_one_ball([1, 2]) == True


def test_move_one_ball_two_elements_rotated():
    """Test with two elements rotated - should return True"""
    assert move_one_ball([2, 1]) == True


def test_move_one_ball_min_at_end():
    """Test with minimum element at the end - should return True"""
    assert move_one_ball([2, 3, 4, 5, 1]) == True


def test_move_one_ball_min_in_middle():
    """Test with minimum element in middle - should return True if sortable"""
    assert move_one_ball([4, 5, 1, 2, 3]) == True
