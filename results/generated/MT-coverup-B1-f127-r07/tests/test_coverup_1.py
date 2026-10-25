# file: project/f127/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

import pytest

from f127 import intersection


@pytest.mark.parametrize(
    ("interval1", "interval2"),
    [
        ((0, 1), (1, 2)),
        ((0, 1), (2, 3)),
    ],
)
def test_intersection_with_nonpositive_length(interval1, interval2):
    assert intersection(interval1, interval2) == "NO"


@pytest.mark.parametrize("length", [2, 3])
def test_intersection_with_prime_length(length):
    assert intersection((0, length), (0, length)) == "YES"


@pytest.mark.parametrize("length", [1, 4])
def test_intersection_with_nonprime_positive_length(length):
    assert intersection((0, length), (0, length)) == "NO"


def test_intersection_exercises_zero_check_after_one_check():
    class PositiveZero(int):
        def __new__(cls):
            return super().__new__(cls, 0)

        def __gt__(self, other):
            return other == 0 or super().__gt__(other)

    class Endpoint(int):
        def __sub__(self, other):
            return PositiveZero()

    assert intersection((0, Endpoint(0)), (0, Endpoint(0))) == "NO"
