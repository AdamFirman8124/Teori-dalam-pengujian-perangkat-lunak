# file: project/f127/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

import pytest

from f127 import intersection


@pytest.mark.parametrize(
    ("interval1", "interval2", "expected"),
    [
        ((0, 1), (2, 3), "NO"),   # Negative intersection length
        ((0, 1), (0, 1), "NO"),   # Length 1
        ((0, 2), (0, 2), "YES"),  # Length 2
        ((0, 4), (0, 4), "NO"),   # Composite length
        ((0, 5), (0, 5), "YES"),  # Prime length greater than 2
    ],
)
def test_intersection_prime_length_branches(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected


def test_intersection_zero_like_positive_length():
    class ZeroLike:
        def __gt__(self, other):
            return other == 0

        def __eq__(self, other):
            return other == 0

    class Endpoint:
        def __lt__(self, other):
            return False

        def __sub__(self, other):
            return ZeroLike()

    endpoint = Endpoint()

    assert intersection((0, endpoint), (0, endpoint)) == "NO"
