# file: project/f094/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [11, 12], [11, 15], [12, 13], [12, 14]]}

from f094 import skjkasdkd


def test_skjkasdkd_empty_list():
    values = []

    assert skjkasdkd(values) == 0
    assert values == []


def test_skjkasdkd_exercises_prime_and_composite_branches():
    values = [2, 4, 3, 3, 9, 13]
    original = values.copy()

    assert skjkasdkd(values) == 4
    assert values == original
