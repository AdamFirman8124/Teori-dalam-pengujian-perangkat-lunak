# file: project/f157/__init__.py:1-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

import pytest

from f157 import right_angle_triangle


def test_right_angle_triangle_true():
    # 3-4-5 triangle: a*a == b*b + c*c branch
    assert right_angle_triangle(3, 4, 5) is True


def test_right_angle_triangle_false():
    # No branch matches, but line 11 still executes
    assert right_angle_triangle(1, 2, 3) is False


def test_right_angle_triangle_other_permutations():
    # b*b == a*a + c*c branch
    assert right_angle_triangle(4, 5, 3) is True
    # c*c == a*a + b*b branch
    assert right_angle_triangle(4, 3, 5) is True
