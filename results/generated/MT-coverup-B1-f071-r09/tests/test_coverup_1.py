# file: project/f071/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5]]}

import pytest

from f071 import triangle_area


@pytest.mark.parametrize(
    ("sides", "expected"),
    [
        ((1, 2, 3), -1),
        ((1, 3, 2), -1),
        ((3, 1, 2), -1),
    ],
)
def test_triangle_area_rejects_each_invalid_triangle_inequality(sides, expected):
    assert triangle_area(*sides) == expected


def test_triangle_area_returns_rounded_heron_area_for_valid_triangle():
    assert triangle_area(3, 4, 5) == 6.0
