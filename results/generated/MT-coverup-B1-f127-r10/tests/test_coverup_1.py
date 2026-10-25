# file: project/f127/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

from f127 import intersection


def test_intersection_with_prime_lengths():
    assert intersection((0, 2), (0, 2)) == "YES"
    assert intersection((0, 3), (0, 3)) == "YES"


def test_intersection_with_nonprime_positive_lengths():
    assert intersection((0, 1), (0, 1)) == "NO"
    assert intersection((0, 4), (0, 4)) == "NO"


def test_intersection_with_no_positive_overlap():
    assert intersection((0, 1), (1, 2)) == "NO"
    assert intersection((0, 1), (2, 3)) == "NO"
