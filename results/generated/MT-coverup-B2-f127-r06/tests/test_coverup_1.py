# file: project/f127/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

import pytest

from f127 import intersection


@pytest.mark.parametrize(
    ("interval1", "interval2", "expected"),
    [
        ((0, 1), (1, 2), "NO"),   # No positive-length intersection.
        ((0, 3), (2, 4), "NO"),   # Intersection length 1.
        ((0, 4), (2, 5), "YES"),  # Intersection length 2.
        ((0, 5), (2, 5), "YES"),  # Intersection length 3, prime.
        ((0, 6), (2, 6), "NO"),   # Intersection length 4, composite.
    ],
)
def test_intersection_prime_and_nonprime_lengths(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected
