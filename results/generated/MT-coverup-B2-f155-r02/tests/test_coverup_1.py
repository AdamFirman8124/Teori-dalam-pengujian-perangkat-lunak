# file: project/f155/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest

from f155 import even_odd_count


def test_even_odd_count_mixed_digits():
    # 123 has one even digit (2) and two odd digits (1, 3)
    result = even_odd_count(123)
    assert result == (1, 2)


def test_even_odd_count_negative_number():
    # Covers the abs() branch: -456 -> digits 4,5,6 -> two even (4,6), one odd (5)
    result = even_odd_count(-456)
    assert result == (2, 1)


def test_even_odd_count_negative_mixed_digits():
    # -1214 -> digits 1,2,1,4 -> two odd (1,1), two even (2,4)
    result = even_odd_count(-1214)
    assert result == (2, 2)


def test_even_odd_count_zero():
    # Zero is a single even digit
    result = even_odd_count(0)
    assert result == (1, 0)


def test_even_odd_count_all_odd():
    result = even_odd_count(13579)
    assert result == (0, 5)


def test_even_odd_count_all_even():
    result = even_odd_count(24680)
    assert result == (5, 0)


def test_even_odd_count_returns_tuple():
    result = even_odd_count(10)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert result == (1, 1)
