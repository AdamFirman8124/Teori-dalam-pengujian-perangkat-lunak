# file: project/f127/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

import pytest

from f127 import intersection


@pytest.mark.parametrize(
    ("interval1", "interval2"),
    [
        ((0, 1), (0, 1)),  # Intersection length 1.
        ((0, 4), (0, 4)),  # Composite intersection length.
        ((0, 1), (2, 3)),  # Negative intersection length.
        ((0, 1), (1, 2)),  # Zero intersection length.
    ],
)
def test_intersection_returns_no(interval1, interval2):
    assert intersection(interval1, interval2) == "NO"


@pytest.mark.parametrize(
    ("interval1", "interval2"),
    [
        ((0, 2), (0, 3)),  # Special-case prime 2.
        ((0, 3), (0, 4)),  # Prime found after loop iteration.
    ],
)
def test_intersection_returns_yes(interval1, interval2):
    assert intersection(interval1, interval2) == "YES"
