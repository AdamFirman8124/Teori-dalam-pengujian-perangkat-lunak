# file: project/f157/__init__.py:1-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

import pytest

from f157 import right_angle_triangle


def test_right_angle_first_operand_true():
    # a*a == b*b + c*c  -> short-circuits on the first operand
    assert right_angle_triangle(5, 3, 4) is True


def test_right_angle_second_operand_true():
    # first operand False, second operand True
    assert right_angle_triangle(3, 5, 4) is True


def test_right_angle_third_operand_true():
    # first two operands False, third operand True
    assert right_angle_triangle(3, 4, 5) is True


def test_not_right_angle_all_operands_false():
    # all three operands False
    assert right_angle_triangle(1, 2, 3) is False


def test_degenerate_zero_sides():
    # 0*0 == 0*0 + 0*0 -> True, exercises the zero-length edge case
    assert right_angle_triangle(0, 0, 0) is True


def test_float_sides():
    assert right_angle_triangle(1.5, 2.0, 2.5) is True


def test_returns_bool_type():
    result = right_angle_triangle(3, 4, 5)
    assert isinstance(result, bool)
