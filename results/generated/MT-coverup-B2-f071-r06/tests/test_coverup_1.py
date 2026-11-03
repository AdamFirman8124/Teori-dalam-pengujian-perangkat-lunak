# file: project/f071/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}

import pytest

from f071 import triangle_area


def test_triangle_area_valid_right_triangle():
    """Covers lines 5-8 (Heron's formula path): 3-4-5 triangle has area 6.0."""
    assert triangle_area(3, 4, 5) == 6.0


def test_triangle_area_valid_rounding():
    """Covers line 7 (rounding): equilateral side 1 has area sqrt(3)/4 ~= 0.43."""
    assert triangle_area(1, 1, 1) == 0.43


def test_triangle_area_invalid_a_plus_b_le_c():
    """Covers line 4 via first sub-condition (a + b <= c)."""
    assert triangle_area(1, 2, 5) == -1


def test_triangle_area_invalid_a_plus_c_le_b():
    """Covers line 4 via second sub-condition (a + c <= b)."""
    assert triangle_area(1, 5, 2) == -1


def test_triangle_area_invalid_b_plus_c_le_a():
    """Covers line 4 via third sub-condition (b + c <= a)."""
    assert triangle_area(5, 1, 2) == -1


def test_triangle_area_degenerate_boundary():
    """Covers line 4 via the equality boundary (a + b == c)."""
    assert triangle_area(1, 2, 3) == -1


def test_triangle_area_valid_boundary_not_triggered():
    """Just below the degenerate boundary the valid path (lines 5-8) is taken."""
    # s = (1 + 2 + 2.9)/2 = 2.95
    # area = sqrt(2.95 * 1.95 * 0.95 * 0.05) ~= 0.5227... -> rounds to 0.52
    assert triangle_area(1, 2, 2.9) == 0.52
