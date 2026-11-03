# file: project/f071/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}

import math

from f071 import triangle_area


def test_triangle_area_invalid_when_a_plus_b_le_c():
    """Covers the 'a + b <= c' branch of the condition (line 3) and the early return (line 4)."""
    assert triangle_area(1, 2, 3) == -1


def test_triangle_area_invalid_when_a_plus_c_le_b():
    """Covers the 'a + c <= b' branch of the condition (line 3) and the early return (line 4)."""
    assert triangle_area(1, 3, 2) == -1


def test_triangle_area_invalid_when_b_plus_c_le_a():
    """Covers the 'b + c <= a' branch of the condition (line 3) and the early return (line 4)."""
    assert triangle_area(3, 1, 2) == -1


def test_triangle_area_valid_right_triangle():
    """Covers lines 5-8 with a 3-4-5 right triangle (area exactly 6.0)."""
    assert triangle_area(3, 4, 5) == 6.0


def test_triangle_area_valid_equilateral_with_rounding():
    """Covers lines 5-8 including the rounding on line 7 (sqrt(3) -> 1.73)."""
    expected = round(math.sqrt(3), 2)
    assert triangle_area(2, 2, 2) == expected == 1.73


def test_triangle_area_valid_scalene_non_integer_result():
    """Covers lines 5-8 with a scalene triangle whose area requires rounding (4-5-6)."""
    s = (4 + 5 + 6) / 2
    expected = round((s * (s - 4) * (s - 5) * (s - 6)) ** 0.5, 2)
    assert triangle_area(4, 5, 6) == expected == 9.92
