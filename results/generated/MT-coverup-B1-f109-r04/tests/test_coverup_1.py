# file: project/f109/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}

from f109 import move_one_ball


def test_move_one_ball_empty_array():
    arr = []
    assert move_one_ball(arr) is True
    assert arr == []


def test_move_one_ball_rotated_sorted_array():
    arr = [3, 4, 1, 2]
    original = arr.copy()

    assert move_one_ball(arr) is True
    assert arr == original


def test_move_one_ball_non_rotated_sorted_array():
    arr = [3, 1, 2, 4]
    original = arr.copy()

    assert move_one_ball(arr) is False
    assert arr == original
