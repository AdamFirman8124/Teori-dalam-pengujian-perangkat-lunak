# file: project/f071/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}

from f071 import triangle_area


def test_triangle_area_invalid_first_condition():
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(1, 2, 3) == -1


def test_triangle_area_invalid_second_condition():
    assert triangle_area(1, 10, 2) == -1


def test_triangle_area_invalid_third_condition():
    assert triangle_area(10, 1, 2) == -1


def test_triangle_area_valid_right_triangle():
    result = triangle_area(3, 4, 5)
    assert result == 6.0
    assert isinstance(result, float)


def test_triangle_area_valid_equilateral_triangle():
    assert triangle_area(2, 2, 2) == 1.73


def test_triangle_area_valid_scalene_triangle():
    assert triangle_area(5, 6, 7) == 14.7
