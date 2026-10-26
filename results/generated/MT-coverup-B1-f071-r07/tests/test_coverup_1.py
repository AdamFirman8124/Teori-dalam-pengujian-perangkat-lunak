# file: project/f071/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}

import pytest

from f071 import triangle_area


@pytest.mark.parametrize(
    "a, b, c",
    [
        (1, 2, 3),   # a + b == c  -> first condition
        (1, 3, 2),   # a + c == b  -> second condition
        (3, 1, 2),   # b + c == a  -> third condition
        (1, 1, 5),   # a + b < c
        (1, 5, 1),   # a + c < b
        (5, 1, 1),   # b + c < a
    ],
)
def test_triangle_area_invalid(a, b, c):
    assert triangle_area(a, b, c) == -1


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (3, 4, 5, 6.0),
        (6, 8, 10, 24.0),
        (2, 2, 2, 1.73),
        (5, 5, 6, 12.0),
    ],
)
def test_triangle_area_valid(a, b, c, expected):
    result = triangle_area(a, b, c)
    assert result == expected
    assert isinstance(result, float)
    assert result > 0


def test_triangle_area_rounding():
    # 1,1,1 -> sqrt(3)/4 = 0.4330127... -> 0.43
    assert triangle_area(1, 1, 1) == 0.43
