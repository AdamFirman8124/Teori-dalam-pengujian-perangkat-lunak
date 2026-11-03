# file: project/f139/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}

"""Tests for f139.special_factorial.

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching or teardown is required to avoid state pollution.
Calling it with n >= 1 executes lines 3-8 (including the loop body);
calling it with n == 0 additionally exercises the branch where the
loop body is skipped entirely.
"""

import math

import pytest

from f139 import special_factorial


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),        # 1!
        (2, 2),        # 1! * 2!
        (3, 12),       # 1! * 2! * 3!
        (4, 288),      # 1! * 2! * 3! * 4!
        (5, 34560),    # 1! * 2! * 3! * 4! * 5!
    ],
)
def test_special_factorial_known_values(n, expected):
    result = special_factorial(n)
    assert result == expected
    assert isinstance(result, int)


def test_special_factorial_zero_skips_loop_body():
    # With n == 0 the loop body never runs, so the initial value 1 is returned.
    assert special_factorial(0) == 1


def test_special_factorial_matches_product_of_factorials():
    n = 8
    expected = 1
    for k in range(1, n + 1):
        expected *= math.factorial(k)
    assert special_factorial(n) == expected


def test_special_factorial_is_strictly_increasing_for_positive_n():
    values = [special_factorial(k) for k in range(1, 7)]
    assert all(a < b for a, b in zip(values, values[1:]))
