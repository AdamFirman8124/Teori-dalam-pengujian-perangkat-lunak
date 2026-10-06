# file: script_71.py:1-17
# asked: {"lines": [12, 13, 14, 15, 16, 17], "branches": [[12, 13], [12, 14]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17], "branches": [[12, 13], [12, 14]]}

import pytest
from script_71 import triangle_area


def test_triangle_area_valid_345():
    """Test valid right triangle 3-4-5"""
    assert triangle_area(3, 4, 5) == 6.00


def test_triangle_area_valid_equilateral():
    """Test valid equilateral triangle"""
    result = triangle_area(5, 5, 5)
    assert result == 10.83


def test_triangle_area_valid_isosceles():
    """Test valid isosceles triangle"""
    result = triangle_area(5, 5, 8)
    assert result == 12.0


def test_triangle_area_invalid_sum_ab_le_c():
    """Test invalid triangle where a + b <= c"""
    assert triangle_area(1, 2, 10) == -1


def test_triangle_area_invalid_sum_ab_equals_c():
    """Test invalid triangle where a + b exactly equals c"""
    assert triangle_area(1, 2, 3) == -1


def test_triangle_area_invalid_sum_ac_le_b():
    """Test invalid triangle where a + c <= b"""
    assert triangle_area(1, 10, 2) == -1


def test_triangle_area_invalid_sum_bc_le_a():
    """Test invalid triangle where b + c <= a"""
    assert triangle_area(10, 1, 2) == -1


def test_triangle_area_valid_small_triangle():
    """Test valid triangle with small sides"""
    result = triangle_area(2, 3, 4)
    assert result == 2.90


def test_triangle_area_valid_large_triangle():
    """Test valid triangle with larger sides"""
    result = triangle_area(13, 14, 15)
    assert result == 84.0
