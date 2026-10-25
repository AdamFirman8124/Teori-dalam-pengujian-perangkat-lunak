# file: project/f109/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}

from f109 import move_one_ball


def test_empty_array_returns_true():
    assert move_one_ball([]) is True


def test_already_sorted_returns_true():
    assert move_one_ball([1, 2, 3, 4]) is True


def test_rotated_sorted_returns_true():
    assert move_one_ball([3, 4, 5, 1, 2]) is True


def test_single_element_returns_true():
    assert move_one_ball([5]) is True


def test_non_rotatable_returns_false():
    assert move_one_ball([2, 1, 3]) is False


def test_rotated_with_duplicates_returns_true():
    assert move_one_ball([2, 2, 1, 2]) is True


def test_unsortable_with_duplicates_returns_false():
    assert move_one_ball([3, 1, 2, 1]) is False
