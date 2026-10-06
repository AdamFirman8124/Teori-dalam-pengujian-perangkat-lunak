# file: script_127.py:1-36
# asked: {"lines": [21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36], "branches": [[22, 23], [22, 24], [24, 25], [24, 26], [26, 27], [26, 29], [27, 26], [27, 28], [34, 35], [34, 36]]}
# gained: {"lines": [21, 22, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36], "branches": [[22, 24], [24, 25], [24, 26], [26, 27], [26, 29], [27, 26], [27, 28], [34, 35], [34, 36]]}

import pytest
from script_127 import intersection


def test_intersection_no_overlap():
    """Test when intervals don't overlap at all."""
    assert intersection((1, 2), (3, 4)) == "NO"


def test_intersection_length_one():
    """Test when intersection length is 1 (not prime)."""
    assert intersection((1, 2), (2, 3)) == "NO"


def test_intersection_length_zero():
    """Test when intervals touch at a single point (length 0)."""
    assert intersection((1, 3), (3, 5)) == "NO"


def test_intersection_length_two_prime():
    """Test when intersection length is 2 (prime)."""
    assert intersection((1, 5), (3, 5)) == "YES"


def test_intersection_length_three_prime():
    """Test when intersection length is 3 (prime)."""
    assert intersection((-3, -1), (-5, 5)) == "YES"


def test_intersection_length_four_not_prime():
    """Test when intersection length is 4 (not prime)."""
    assert intersection((1, 5), (1, 5)) == "NO"


def test_intersection_length_five_prime():
    """Test when intersection length is 5 (prime)."""
    assert intersection((0, 10), (5, 10)) == "YES"


def test_intersection_length_six_not_prime():
    """Test when intersection length is 6 (not prime)."""
    assert intersection((0, 10), (4, 10)) == "NO"


def test_intersection_negative_intervals():
    """Test with negative intervals."""
    assert intersection((-10, -5), (-7, -2)) == "YES"


def test_intersection_length_seven_prime():
    """Test with intersection length of 7 (prime)."""
    assert intersection((1, 10), (3, 10)) == "YES"


def test_intersection_same_intervals():
    """Test when both intervals are identical with prime length."""
    assert intersection((5, 10), (5, 10)) == "YES"


def test_intersection_length_eight_not_prime():
    """Test when intersection length is 8 (not prime)."""
    assert intersection((0, 10), (2, 10)) == "NO"


def test_intersection_length_nine_not_prime():
    """Test when intersection length is 9 (not prime)."""
    assert intersection((0, 10), (1, 10)) == "NO"


def test_intersection_length_eleven_prime():
    """Test when intersection length is 11 (prime)."""
    assert intersection((0, 15), (4, 15)) == "YES"
