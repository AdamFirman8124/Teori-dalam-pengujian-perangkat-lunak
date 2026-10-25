# file: project/f045/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f045 import triangle_area


def test_triangle_area_executes_return_line():
    result = triangle_area(4, 3)
    assert result == 6.0
    assert isinstance(result, float)


def test_triangle_area_zero_base():
    assert triangle_area(0, 5) == 0.0


def test_triangle_area_fractional():
    assert triangle_area(2.5, 4.0) == 5.0
