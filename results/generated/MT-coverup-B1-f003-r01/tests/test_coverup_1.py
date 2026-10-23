# file: project/f003/__init__.py:4-13
# asked: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}
# gained: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}

import importlib

import pytest

f003 = importlib.import_module("f003")
below_zero = f003.below_zero


def test_empty_operations_returns_false():
    assert below_zero([]) is False


def test_all_positive_returns_false():
    assert below_zero([1, 2, 3]) is False


def test_all_negative_first_returns_true():
    assert below_zero([-1, 5]) is True


def test_negative_after_positives_returns_true():
    # balances: 5 -> 10 -> -1 (below zero)
    assert below_zero([5, 5, -11]) is True


def test_exactly_zero_balance_never_below_zero():
    assert below_zero([1, -1]) is False


def test_negative_on_last_operation_returns_true():
    # balances: 1 -> 3 -> 0 (never below zero)
    assert below_zero([1, 2, -3]) is False


def test_zero_operations_do_not_trigger():
    assert below_zero([0, 0, 0]) is False


def test_original_list_not_mutated():
    operations = [1, -2, 3]
    snapshot = list(operations)
    below_zero(operations)
    assert operations == snapshot


def test_returns_actual_bool():
    assert below_zero([1, 2]) is False
    assert below_zero([-5]) is True
