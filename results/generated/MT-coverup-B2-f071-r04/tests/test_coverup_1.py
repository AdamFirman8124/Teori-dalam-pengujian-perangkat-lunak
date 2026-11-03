# file: project/f071/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}

import pytest

from f071 import triangle_area


def test_triangle_area_invalid_returns_minus_one():
    """Lines 3-4: each short-circuit branch of the invalidity condition,
    including the degenerate (equality) boundary, must yield -1."""
    assert triangle_area(1, 2, 10) == -1   # a + b <= c
    assert triangle_area(1, 10, 2) == -1   # a + c <= b
    assert triangle_area(10, 1, 2) == -1   # b + c <= a
    assert triangle_area(3, 4, 7) == -1    # degenerate: a + b == c


def test_triangle_area_valid_heron():
    """Lines 5-8: a valid triangle computes the rounded Heron's-formula area."""
    # 3-4-5 right triangle: s = 6, area = sqrt(6*3*2*1) = 6.0
    assert triangle_area(3, 4, 5) == 6.0
    # Equilateral unit triangle: s = 1.5, area = sqrt(0.1875) -> 0.43
    assert triangle_area(1, 1, 1) == 0.43
    # Isosceles: s = 3.5, area = sqrt(3.9375) -> 1.98
    assert triangle_area(2, 2, 3) == 1.98
    # Result must be rounded to 2 decimal places
    result = triangle_area(7, 8, 9)
    assert result == round((12 * 5 * 4 * 3) ** 0.5, 2)
    assert result == pytest.approx(26.83)
