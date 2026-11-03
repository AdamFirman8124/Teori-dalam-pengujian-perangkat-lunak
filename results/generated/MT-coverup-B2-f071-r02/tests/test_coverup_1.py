# file: project/f071/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}

import pytest

from f071 import triangle_area


def test_triangle_area_invalid_ab_le_c():
    """Line 3-4: 'a + b <= c' branch triggers the -1 early return."""
    assert triangle_area(1, 2, 10) == -1


def test_triangle_area_invalid_ac_le_b():
    """Line 3-4: 'a + c <= b' branch triggers the -1 early return."""
    assert triangle_area(1, 10, 2) == -1


def test_triangle_area_invalid_bc_le_a():
    """Line 3-4: 'b + c <= a' branch triggers the -1 early return."""
    assert triangle_area(10, 1, 2) == -1


def test_triangle_area_degenerate():
    """Line 3-4: degenerate triangle (a + b == c) is also rejected."""
    assert triangle_area(1, 2, 3) == -1


def test_triangle_area_right_triangle():
    """Lines 5-8: valid 3-4-5 right triangle has area exactly 6.0."""
    assert triangle_area(3, 4, 5) == 6.0


def test_triangle_area_equilateral_rounding():
    """Lines 5-8: equilateral side 2 -> sqrt(3) rounded to 1.73."""
    assert triangle_area(2, 2, 2) == 1.73


def test_triangle_area_scalene_rounding():
    """Lines 5-8: scalene 4-5-6 -> sqrt(98.4375) rounded to 9.92."""
    assert triangle_area(4, 5, 6) == pytest.approx(9.92)
