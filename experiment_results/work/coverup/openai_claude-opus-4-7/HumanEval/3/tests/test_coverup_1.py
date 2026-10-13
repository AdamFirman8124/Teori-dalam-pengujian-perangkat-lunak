# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

from typing import List
import pytest

from script_3 import below_zero


def test_below_zero_stays_non_negative():
    assert below_zero([1, 2, 3]) is False


def test_below_zero_goes_negative_midway():
    assert below_zero([1, 2, -4, 5]) is True


def test_below_zero_empty_operations():
    assert below_zero([]) is False


def test_below_zero_negative_on_first_operation():
    assert below_zero([-1]) is True


def test_below_zero_returns_early():
    # negative balance occurs early; the rest of the list must not matter
    assert below_zero([1, -2, 100]) is True


def test_below_zero_ends_exactly_at_zero():
    assert below_zero([5, -5]) is False
