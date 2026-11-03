# file: project/f157/__init__.py:1-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

"""Tests for f157.right_angle_triangle.

The function under test is pure (no I/O, no module state, no side effects),
so no monkeypatching/teardown is required; each test is fully isolated.
The tests below exercise every branch of the short-circuiting ``or`` chain
on line 11, which is the only executable line of the function.
"""

import pytest

from f157 import right_angle_triangle


def test_right_angle_triangle_first_branch_true():
    """a*a == b*b + c*c is True -> short-circuits on the first condition."""
    # 5*5 == 3*3 + 4*4  ->  25 == 25
    assert right_angle_triangle(5, 3, 4) is True


def test_right_angle_triangle_second_branch_true():
    """First condition False, b*b == a*a + c*c True -> second condition hit."""
    # 3*3 != 5*5 + 4*4, but 5*5 == 3*3 + 4*4  ->  25 == 25
    assert right_angle_triangle(3, 5, 4) is True


def test_right_angle_triangle_third_branch_true():
    """First two conditions False, c*c == a*a + b*b True -> third condition hit."""
    # 4*4 != 3*3 + 5*5, 3*3 != 4*4 + 5*5, but 5*5 == 4*4 + 3*3  ->  25 == 25
    assert right_angle_triangle(4, 3, 5) is True


def test_right_angle_triangle_all_branches_false():
    """No condition holds -> the whole expression evaluates to False."""
    # 1 != 4+9, 4 != 1+9, 9 != 1+4
    assert right_angle_triangle(1, 2, 3) is False


def test_right_angle_triangle_floats_third_branch():
    """Works with floats; exercises the third condition with non-integers."""
    # 2.5*2.5 != 6.0*6.0 + 6.5*6.5, 6.0*6.0 != 2.5*2.5 + 6.5*6.5,
    # 6.5*6.5 == 2.5*2.5 + 6.0*6.0  ->  42.25 == 42.25
    assert right_angle_triangle(2.5, 6.0, 6.5) is True


def test_right_angle_triangle_floats_all_false():
    """Floats that do not form a right triangle return False."""
    assert right_angle_triangle(1.5, 2.5, 3.5) is False


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (5, 3, 4, True),    # a is the hypotenuse
        (3, 5, 4, True),    # b is the hypotenuse
        (4, 3, 5, True),    # c is the hypotenuse
        (1, 2, 3, False),   # not a right triangle
        (2, 2, 2, False),   # equilateral, not right
        (0, 0, 0, True),    # degenerate: 0 == 0 + 0
    ],
)
def test_right_angle_triangle_parametrized(a, b, c, expected):
    """Parametrized sweep over all branches of the or-chain."""
    assert right_angle_triangle(a, b, c) is expected
