# file: project/f046/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}

import pytest

from f046 import fib4


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),   # n < 4, returns results[0]
        (1, 0),   # n < 4, returns results[1]
        (2, 2),   # n < 4, returns results[2]
        (3, 0),   # n < 4, returns results[3]
    ],
)
def test_fib4_base_cases(n, expected):
    """Covers lines 3-5: initialization and the n < 4 early-return branch."""
    assert fib4(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (4, 2),    # loop runs exactly once
        (5, 4),    # loop runs twice
        (6, 8),    # loop runs three times
        (7, 14),   # loop runs four times
        (8, 28),   # loop runs five times
        (10, 104), # larger n to exercise repeated append/pop
    ],
)
def test_fib4_iterative_cases(n, expected):
    """Covers lines 7-9 and 11: the for-loop branch and final return."""
    assert fib4(n) == expected


def test_fib4_matches_sum_of_previous_four():
    """Verify the recurrence: each result is the sum of the previous four values."""
    values = [fib4(i) for i in range(12)]
    assert values[:4] == [0, 0, 2, 0]
    for i in range(4, 12):
        assert values[i] == values[i - 1] + values[i - 2] + values[i - 3] + values[i - 4]
