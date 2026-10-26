# file: project/f157/__init__.py:1-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

from f157 import right_angle_triangle


def test_right_angle_hypotenuse_a():
    assert right_angle_triangle(5, 3, 4) is True
    assert right_angle_triangle(5, 4, 3) is True


def test_right_angle_hypotenuse_b():
    assert right_angle_triangle(3, 5, 4) is True
    assert right_angle_triangle(4, 5, 3) is True


def test_right_angle_hypotenuse_c():
    assert right_angle_triangle(3, 4, 5) is True
    assert right_angle_triangle(4, 3, 5) is True


def test_non_right_angle():
    assert right_angle_triangle(1, 2, 3) is False
    assert right_angle_triangle(2, 3, 4) is False
    assert right_angle_triangle(4, 5, 6) is False
