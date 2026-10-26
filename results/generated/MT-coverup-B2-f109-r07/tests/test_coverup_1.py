# file: project/f109/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14], "branches": [[3, 4], [3, 5], [11, 12], [11, 14], [12, 11], [12, 13]]}

from f109 import move_one_ball


def test_empty_array_returns_true():
    arr = []
    result = move_one_ball(arr)
    assert result is True
    assert arr == []


def test_single_element_returns_true():
    arr = [7]
    result = move_one_ball(arr)
    assert result is True
    assert arr == [7]


def test_already_sorted_returns_true():
    arr = [1, 2, 3, 4, 5]
    snapshot = list(arr)
    result = move_one_ball(arr)
    assert result is True
    assert arr == snapshot


def test_rotated_sorted_returns_true():
    arr = [3, 4, 5, 1, 2]
    snapshot = list(arr)
    result = move_one_ball(arr)
    assert result is True
    assert arr == snapshot


def test_rotated_single_shift_returns_true():
    arr = [2, 3, 4, 5, 1]
    result = move_one_ball(arr)
    assert result is True


def test_unsortable_returns_false():
    arr = [2, 1, 3]
    snapshot = list(arr)
    result = move_one_ball(arr)
    assert result is False
    assert arr == snapshot


def test_unsortable_second_case_returns_false():
    arr = [1, 3, 2]
    result = move_one_ball(arr)
    assert result is False


def test_reverse_sorted_returns_false():
    arr = [5, 4, 3, 2, 1]
    result = move_one_ball(arr)
    assert result is False
