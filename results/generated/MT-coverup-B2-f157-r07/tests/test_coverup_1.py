# file: project/f157/__init__.py:1-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

from f157 import right_angle_triangle


def test_a_is_hypotenuse():
    assert right_angle_triangle(5, 3, 4) is True
    assert right_angle_triangle(5, 3, 4) == True


def test_b_is_hypotenuse():
    assert right_angle_triangle(3, 5, 4) is True
    assert right_angle_triangle(3, 5, 4) == True


def test_c_is_hypotenuse():
    assert right_angle_triangle(3, 4, 5) is True
    assert right_angle_triangle(3, 4, 5) == True


def test_not_right_angle():
    assert right_angle_triangle(1, 2, 3) is False
    assert right_angle_triangle(1, 2, 3) == False
