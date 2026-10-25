# file: project/f045/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f045 import triangle_area


def test_triangle_area_basic():
    assert triangle_area(4, 6) == 12.0


def test_triangle_area_returns_float():
    result = triangle_area(3, 5)
    assert result == 7.5
    assert isinstance(result, float)


@pytest.mark.parametrize(
    "a, h, expected",
    [
        (0, 10, 0.0),
        (10, 0, 0.0),
        (1, 1, 0.5),
        (2.5, 4, 5.0),
        (-3, 4, -6.0),
    ],
)
def test_triangle_area_parametrized(a, h, expected):
    assert triangle_area(a, h) == expected
