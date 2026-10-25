# file: project/f094/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}

from f094 import skjkasdkd


def test_skjkasdkd_covers_prime_and_composite_candidates():
    assert skjkasdkd([1, 2, 4, 5, 3, 29, 25]) == 11


def test_skjkasdkd_with_empty_list():
    assert skjkasdkd([]) == 0
