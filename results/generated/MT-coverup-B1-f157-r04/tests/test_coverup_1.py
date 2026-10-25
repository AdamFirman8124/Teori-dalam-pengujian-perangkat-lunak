# file: project/f157/__init__.py:1-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

import pytest

from f157 import right_angle_triangle


def test_first_condition_true():
    # a is the hypotenuse
    assert right_angle_triangle(5, 3, 4) is True


def test_second_condition_true():
    # b is the hypotenuse (first condition must be False)
    assert right_angle_triangle(3, 5, 4) is True


def test_third_condition_true():
    # c is the hypotenuse (first two conditions must be False)
    assert right_angle_triangle(3, 4, 5) is True


def test_all_conditions_false():
    assert right_angle_triangle(1, 2, 3) is False


def test_degenerate_and_zero_sides():
    # (0, 0, 0) satisfies the first condition: 0 == 0 + 0
    assert right_angle_triangle(0, 0, 0) is True
    # (0, 1, 1) satisfies the second condition: 1 == 0 + 1
    assert right_angle_triangle(0, 1, 1) is True
    # (0, 1, 2) satisfies none of the conditions
    assert right_angle_triangle(0, 1, 2) is False


def test_float_sides():
    assert right_angle_triangle(1.5, 2.0, 2.5) is True
    assert right_angle_triangle(1.5, 2.0, 2.6) is False


def test_returns_bool_not_truthy():
    result = right_angle_triangle(3, 4, 5)
    assert isinstance(result, bool)
    assert result is True
