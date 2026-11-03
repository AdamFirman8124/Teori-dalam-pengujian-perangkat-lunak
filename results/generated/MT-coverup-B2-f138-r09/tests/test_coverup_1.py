# file: project/f138/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f138 import is_equal_to_sum_even


def test_true_when_even_and_at_least_8():
    # even (n % 2 == 0 -> True) and n >= 8 -> True: covers full 'and' expression
    assert is_equal_to_sum_even(8) is True
    assert is_equal_to_sum_even(10) is True
    assert is_equal_to_sum_even(100) is True


def test_false_when_even_but_below_8():
    # even (n % 2 == 0 -> True) but n >= 8 is False: covers second branch of 'and'
    assert is_equal_to_sum_even(0) is False
    assert is_equal_to_sum_even(2) is False
    assert is_equal_to_sum_even(4) is False
    assert is_equal_to_sum_even(6) is False


def test_false_when_odd():
    # odd: n % 2 == 0 is False, 'and' short-circuits without evaluating n >= 8
    assert is_equal_to_sum_even(1) is False
    assert is_equal_to_sum_even(7) is False
    assert is_equal_to_sum_even(9) is False


def test_false_when_negative_even():
    # negative even number: even but below 8
    assert is_equal_to_sum_even(-8) is False
    assert is_equal_to_sum_even(-2) is False


def test_false_when_negative_odd():
    # negative odd number: odd, short-circuits the 'and'
    assert is_equal_to_sum_even(-1) is False
    assert is_equal_to_sum_even(-7) is False
