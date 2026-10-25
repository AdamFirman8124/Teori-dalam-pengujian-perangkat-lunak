# file: project/f109/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}

from f109 import move_one_ball


def test_move_one_ball_empty_array():
    assert move_one_ball([]) is True


def test_move_one_ball_rotated_sorted_array():
    arr = [3, 4, 1, 2]

    assert move_one_ball(arr) is True
    assert arr == [3, 4, 1, 2]


def test_move_one_ball_unsortable_by_single_rotation():
    arr = [3, 1, 4, 2]

    assert move_one_ball(arr) is False
    assert arr == [3, 1, 4, 2]
