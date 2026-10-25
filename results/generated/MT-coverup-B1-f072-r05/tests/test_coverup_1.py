# file: project/f072/__init__.py:1-12
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}

from f072 import will_it_fly


def test_will_it_fly_rejects_overweight_sequence():
    assert will_it_fly([1, 2, 1], 3) is False


def test_will_it_fly_rejects_non_palindrome():
    assert will_it_fly([1, 2, 3], 6) is False


def test_will_it_fly_accepts_palindrome_within_weight_limit():
    assert will_it_fly([1, 2, 3, 2, 1], 9) is True


def test_will_it_fly_accepts_empty_sequence():
    assert will_it_fly([], 0) is True
