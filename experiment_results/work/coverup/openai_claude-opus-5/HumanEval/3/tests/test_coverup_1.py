# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

import pytest

from script_3 import below_zero


def test_below_zero_all_positive_returns_false():
    assert below_zero([1, 2, 3]) is False


def test_below_zero_went_negative_then_recovered_returns_true():
    assert below_zero([1, 2, -4, 5]) is True


def test_below_zero_starts_negative_returns_true():
    assert below_zero([-1]) is True


def test_below_zero_exactly_zero_returns_false():
    assert below_zero([1, -1, 0, 5]) is False


def test_below_zero_empty_list_returns_false():
    assert below_zero([]) is False
