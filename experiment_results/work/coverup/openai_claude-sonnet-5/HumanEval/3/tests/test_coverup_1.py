# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

import importlib
import sys

import pytest

MODULE_NAME = "script_3"


@pytest.fixture
def below_zero():
    if MODULE_NAME not in sys.modules:
        sys.modules[MODULE_NAME] = importlib.import_module(MODULE_NAME)
    mod = sys.modules[MODULE_NAME]
    return mod.below_zero


def test_empty_operations_returns_false(below_zero):
    assert below_zero([]) is False


def test_all_deposits_returns_false(below_zero):
    assert below_zero([1, 2, 3]) is False


def test_balance_reaches_exactly_zero_returns_false(below_zero):
    assert below_zero([5, -5]) is False
    assert below_zero([1, -1, 2, -2]) is False


def test_drops_below_zero_midway_returns_true(below_zero):
    assert below_zero([1, 2, -4, 5]) is True


def test_single_negative_first_returns_true(below_zero):
    assert below_zero([-1]) is True


def test_never_goes_negative_returns_false(below_zero):
    assert below_zero([10, -5, -5, 100, -99]) is False
