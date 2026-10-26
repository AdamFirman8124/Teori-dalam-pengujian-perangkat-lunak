# file: project/f109/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}

from f109 import move_one_ball


def test_move_one_ball_empty():
    assert move_one_ball([]) is True


def test_move_one_ball_single_element():
    assert move_one_ball([5]) is True


def test_move_one_ball_already_sorted():
    assert move_one_ball([1, 2, 3, 4, 5]) is True


def test_move_one_ball_rotated_sorted():
    assert move_one_ball([3, 4, 5, 1, 2]) is True


def test_move_one_ball_min_at_start_but_unsorted():
    assert move_one_ball([1, 3, 2]) is False


def test_move_one_ball_not_achievable():
    assert move_one_ball([3, 1, 2, 4]) is False


def test_move_one_ball_duplicates():
    assert move_one_ball([2, 2, 1, 2]) is True
    assert move_one_ball([1, 2, 1, 2]) is False


def test_move_one_ball_all_equal():
    assert move_one_ball([7, 7, 7]) is True


def test_move_one_ball_descending():
    assert move_one_ball([5, 4, 3, 2, 1]) is False
