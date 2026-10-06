# file: script_71.py:1-17
# asked: {"lines": [12, 13, 14, 15, 16, 17], "branches": [[12, 13], [12, 14]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17], "branches": [[12, 13], [12, 14]]}

import pytest
from script_71 import triangle_area


def test_triangle_area_valid_triangle():
    """Test valid triangle returns correct area"""
    result = triangle_area(3, 4, 5)
    assert result == 6.00
    

def test_triangle_area_invalid_sum_ab_less_than_c():
    """Test invalid triangle where a + b <= c"""
    result = triangle_area(1, 2, 10)
    assert result == -1


def test_triangle_area_invalid_sum_ac_less_than_b():
    """Test invalid triangle where a + c <= b"""
    result = triangle_area(1, 10, 2)
    assert result == -1


def test_triangle_area_invalid_sum_bc_less_than_a():
    """Test invalid triangle where b + c <= a"""
    result = triangle_area(10, 1, 2)
    assert result == -1


def test_triangle_area_equilateral():
    """Test equilateral triangle"""
    result = triangle_area(5, 5, 5)
    s = (5 + 5 + 5) / 2
    expected = round((s * (s - 5) * (s - 5) * (s - 5)) ** 0.5, 2)
    assert result == expected


def test_triangle_area_isosceles():
    """Test isosceles triangle"""
    result = triangle_area(5, 5, 6)
    s = (5 + 5 + 6) / 2
    expected = round((s * (s - 5) * (s - 5) * (s - 6)) ** 0.5, 2)
    assert result == expected


def test_triangle_area_edge_case_equal_sum():
    """Test edge case where sum equals third side"""
    result = triangle_area(1, 2, 3)
    assert result == -1
