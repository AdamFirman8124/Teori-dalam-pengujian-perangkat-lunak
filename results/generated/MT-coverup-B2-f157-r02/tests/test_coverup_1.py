# file: project/f157/__init__.py:1-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

import pytest

from f157 import right_angle_triangle


def test_hypotenuse_is_first_side():
    """a is the hypotenuse: first disjunct (a*a == b*b + c*c) is True."""
    assert right_angle_triangle(5, 3, 4) is True


def test_hypotenuse_is_second_side():
    """b is the hypotenuse: first disjunct False, second disjunct (b*b == a*a + c*c) is True."""
    assert right_angle_triangle(3, 5, 4) is True


def test_hypotenuse_is_third_side():
    """c is the hypotenuse: first two disjuncts False, third disjunct (c*c == a*a + b*b) is True."""
    assert right_angle_triangle(3, 4, 5) is True


def test_not_right_triangle():
    """No side is the hypotenuse: all three disjuncts are False."""
    assert right_angle_triangle(1, 2, 3) is False


def test_non_right_triangle_all_disjuncts_evaluated():
    """A valid but non-right triangle: every disjunct is evaluated and False."""
    assert right_angle_triangle(4, 5, 6) is False
