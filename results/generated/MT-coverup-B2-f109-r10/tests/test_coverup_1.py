# file: project/f109/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}

import pytest

from f109 import move_one_ball


def test_empty_array_returns_true():
    assert move_one_ball([]) is True


def test_single_element_returns_true():
    assert move_one_ball([7]) is True


def test_already_sorted_returns_true():
    arr = [1, 2, 3, 4, 5]
    assert move_one_ball(arr) is True
    # postcondition: input not mutated
    assert arr == [1, 2, 3, 4, 5]


def test_valid_rotation_returns_true():
    arr = [3, 4, 5, 1, 2]
    assert move_one_ball(arr) is True
    assert arr == [3, 4, 5, 1, 2]


def test_rotation_with_duplicates_returns_true():
    assert move_one_ball([2, 2, 3, 1, 2]) is True


def test_non_rotation_returns_false():
    arr = [1, 3, 2, 4]
    assert move_one_ball(arr) is False
    assert arr == [1, 3, 2, 4]


def test_descending_returns_false():
    assert move_one_ball([5, 4, 3, 2, 1]) is False


def test_minimum_at_end_rotation_returns_true():
    assert move_one_ball([2, 3, 4, 1]) is True


def test_returns_bool_type():
    assert isinstance(move_one_ball([1, 2]), bool)
    assert isinstance(move_one_ball([2, 1, 3]), bool)
