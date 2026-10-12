# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

import pytest

from script_3 import below_zero


def test_empty_operations_no_fall_below():
    assert below_zero([]) is False


def test_all_deposits():
    assert below_zero([1, 2, 3]) is False
    assert below_zero([10, 5]) is False


def test_exact_zero_is_not_below_zero():
    assert below_zero([5, -5, 2]) is False
    assert below_zero([3, -2, -1]) is False


def test_falls_below_zero_in_middle():
    assert below_zero([1, 2, -4, 5]) is True


def test_falls_below_zero_immediately():
    assert below_zero([-1]) is True
    assert below_zero([-3, 3]) is True


def test_stays_negative_multiple_steps():
    assert below_zero([0, -1, -2, 10]) is True


def test_does_not_mutate_input():
    operations = [1, 2, -4, 5]
    copy = list(operations)
    assert below_zero(operations) is True
    assert operations == copy


def test_module_importable_and_callable():
    assert callable(below_zero)
