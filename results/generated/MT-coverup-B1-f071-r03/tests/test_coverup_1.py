# file: project/f071/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}

import pytest

from f071 import triangle_area


@pytest.mark.parametrize(
    ("sides", "expected"),
    [
        ((1, 1, 2), -1),
        ((1, 3, 2), -1),
        ((3, 1, 2), -1),
    ],
)
def test_triangle_area_rejects_invalid_triangles(sides, expected):
    assert triangle_area(*sides) == expected


def test_triangle_area_calculates_valid_triangle():
    assert triangle_area(3, 4, 5) == 6.0
