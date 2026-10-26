# file: project/f155/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest

from f155 import even_odd_count


def test_even_digits_only():
    assert even_odd_count(2468) == (4, 0)


def test_odd_digits_only():
    assert even_odd_count(1357) == (0, 4)


def test_mixed_digits():
    assert even_odd_count(123456) == (3, 3)


def test_negative_number_uses_abs():
    assert even_odd_count(-123) == (1, 2)


def test_zero_is_even():
    assert even_odd_count(0) == (1, 0)
