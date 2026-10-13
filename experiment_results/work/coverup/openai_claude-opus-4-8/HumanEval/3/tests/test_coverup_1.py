# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

import pytest

from script_3 import below_zero


def test_below_zero_all_positive():
    assert below_zero([1, 2, 3]) is False


def test_below_zero_negative_midway():
    assert below_zero([1, 2, -4, 5]) is True


def test_below_zero_empty_list():
    assert below_zero([]) is False


def test_below_zero_zero_balance_ok():
    assert below_zero([1, -1, 2, -2]) is False


def test_below_zero_first_op_negative():
    assert below_zero([-1]) is True


def test_below_zero_returns_early_after_negative():
    ops = [5, -10, 100, -200]
    assert below_zero(ops) is True
    # original list must be unchanged (no mutation / pollution)
    assert ops == [5, -10, 100, -200]


def test_below_zero_does_not_mutate_input_when_balanced():
    ops = [1, 2, -1, 2]
    before = list(ops)
    assert below_zero(ops) is False
    assert ops == before


@pytest.mark.parametrize(
    "operations, expected",
    [
        ([], False),
        ([3], False),
        ([0, 0], False),
        ([2, -2], False),
        ([2, -3], True),
        ([1, 2, -4, 5], True),
        ([-5, 5], True),
        ([10, -5, -6], True),
        ([10, -5, -5], False),
    ],
)
def test_below_zero_parametrized(operations, expected):
    assert below_zero(operations) is expected
