# file: project/f155/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

from f155 import even_odd_count


def test_even_odd_count_mixed_digits():
    assert even_odd_count(12345) == (2, 3)


def test_even_odd_count_all_even_and_zero():
    assert even_odd_count(24680) == (5, 0)
    assert even_odd_count(0) == (1, 0)


def test_even_odd_count_all_odd_and_negative():
    assert even_odd_count(13579) == (0, 5)
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-13579) == (0, 5)
