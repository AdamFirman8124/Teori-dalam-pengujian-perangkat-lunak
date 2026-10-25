# file: project/f157/__init__.py:1-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

from f157 import right_angle_triangle


def test_right_angle_triangle_when_first_condition_is_true():
    assert right_angle_triangle(5, 3, 4) is True


def test_right_angle_triangle_when_second_condition_is_true():
    assert right_angle_triangle(3, 5, 4) is True


def test_right_angle_triangle_when_third_condition_is_true():
    assert right_angle_triangle(3, 4, 5) is True


def test_right_angle_triangle_when_no_condition_is_true():
    assert right_angle_triangle(1, 2, 3) is False
