# file: project/f109/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}

from f109 import move_one_ball


def test_move_one_ball_empty_list():
    assert move_one_ball([]) is True


def test_move_one_ball_rotated_sorted_list():
    arr = [3, 4, 1, 2]
    original = arr.copy()

    assert move_one_ball(arr) is True
    assert arr == original


def test_move_one_ball_non_rotatable_list():
    arr = [2, 1, 3]
    original = arr.copy()

    assert move_one_ball(arr) is False
    assert arr == original
