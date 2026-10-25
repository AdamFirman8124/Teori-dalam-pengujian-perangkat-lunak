# file: project/f155/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

from f155 import even_odd_count


def test_even_odd_count_with_mixed_negative_number():
    assert even_odd_count(-123456) == (3, 3)


def test_even_odd_count_with_zero():
    assert even_odd_count(0) == (1, 0)
