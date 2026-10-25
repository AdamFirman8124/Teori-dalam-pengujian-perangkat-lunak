# file: project/f045/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f045 import triangle_area


def test_triangle_area():
    assert triangle_area(3, 4) == 6.0
