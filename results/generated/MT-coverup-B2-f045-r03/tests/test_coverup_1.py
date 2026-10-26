# file: project/f045/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f045 import triangle_area


def test_triangle_area_basic():
    assert triangle_area(4, 3) == 6.0


def test_triangle_area_float_and_zero():
    assert triangle_area(0, 5) == 0.0
    assert triangle_area(5, 0) == 0.0
    assert triangle_area(2.5, 4.0) == 5.0
    assert triangle_area(3, 3) == 4.5
