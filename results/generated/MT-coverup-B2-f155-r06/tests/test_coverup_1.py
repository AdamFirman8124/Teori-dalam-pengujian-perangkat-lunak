# file: project/f155/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest

from f155 import even_odd_count


def test_even_odd_count_all_even_digits():
    assert even_odd_count(2468) == (4, 0)


def test_even_odd_count_all_odd_digits():
    assert even_odd_count(1357) == (0, 4)


def test_even_odd_count_mixed_digits():
    assert even_odd_count(123456) == (3, 3)


def test_even_odd_count_negative_number_uses_absolute_value():
    assert even_odd_count(-123456) == (3, 3)


def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)


def test_even_odd_count_single_digit():
    assert even_odd_count(7) == (0, 1)
    assert even_odd_count(8) == (1, 0)


def test_even_odd_count_returns_tuple_of_ints():
    result = even_odd_count(1234)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(count, int) for count in result)
    assert sum(result) == len(str(abs(1234)))
