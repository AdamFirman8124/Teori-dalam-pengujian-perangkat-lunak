# file: project/f157/__init__.py:1-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

from f157 import right_angle_triangle


def test_right_angle_first_side_is_hypotenuse():
    """a*a == b*b + c*c is True -> first disjunct short-circuits to True."""
    # 5**2 == 3**2 + 4**2
    assert right_angle_triangle(5, 3, 4) is True


def test_right_angle_second_side_is_hypotenuse():
    """First disjunct False, b*b == a*a + c*c True -> second branch taken."""
    # 3**2 != 5**2 + 4**2, but 5**2 == 3**2 + 4**2
    assert right_angle_triangle(3, 5, 4) is True


def test_right_angle_third_side_is_hypotenuse():
    """First two disjuncts False, c*c == a*a + b*b True -> third branch taken."""
    # 3**2 != 4**2 + 5**2, 4**2 != 3**2 + 5**2, but 5**2 == 3**2 + 4**2
    assert right_angle_triangle(3, 4, 5) is True


def test_not_right_angle_all_disjuncts_false():
    """All three disjuncts evaluate False -> returns False."""
    assert right_angle_triangle(1, 2, 3) is False


def test_equilateral_not_right_angle():
    """Equilateral sides: every disjunct is False."""
    assert right_angle_triangle(2, 2, 2) is False


def test_right_angle_with_float_sides():
    """Float sides are supported: 2.5**2 + 6.0**2 == 6.5**2."""
    assert right_angle_triangle(2.5, 6.0, 6.5) is True
