# file: project/f071/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}

import math

import pytest

from f071 import triangle_area


def test_triangle_area_valid_right_triangle():
    """Covers lines 3 (condition false), 5-8: valid triangle computes area."""
    result = triangle_area(3, 4, 5)
    assert result == 6.0
    assert isinstance(result, float)
    assert result == round(math.sqrt(6 * (6 - 3) * (6 - 4) * (6 - 5)), 2)


def test_triangle_area_valid_scalene_triangle():
    """Covers lines 5-7 again with a non-integer area requiring rounding."""
    # Triangle with sides 2, 3, 4: s = 4.5
    # area = sqrt(4.5 * 2.5 * 1.5 * 0.5) = sqrt(8.4375) ≈ 2.9047... -> 2.9
    result = triangle_area(2, 3, 4)
    expected = round(math.sqrt(4.5 * 2.5 * 1.5 * 0.5), 2)
    assert result == pytest.approx(2.90, abs=1e-9)
    assert result == expected
    assert result != -1


def test_triangle_area_invalid_first_condition():
    """Covers line 3-4 short-circuit: a + b <= c (degenerate triangle)."""
    assert triangle_area(1, 2, 3) == -1


def test_triangle_area_invalid_second_condition():
    """Covers line 3 branch: a + b > c but a + c <= b."""
    assert triangle_area(2, 4, 1) == -1


def test_triangle_area_invalid_third_condition():
    """Covers line 3 branch: a + b > c, a + c > b, but b + c <= a."""
    assert triangle_area(5, 1, 1) == -1


def test_triangle_area_equilateral():
    """Covers full valid path with an equilateral triangle."""
    result = triangle_area(1, 1, 1)
    expected = round(math.sqrt(1.5 * 0.5 * 0.5 * 0.5), 2)
    assert result == expected
    assert result > 0
