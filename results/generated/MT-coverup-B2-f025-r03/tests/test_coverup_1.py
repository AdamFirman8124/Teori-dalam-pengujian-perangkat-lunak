# file: project/f025/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}

"""Tests for f025.factorize.

The function under test is pure (no module state, no I/O), so no
monkeypatching/teardown is required; each test only relies on its own
inputs and leaves no state behind.
"""

import pytest

from f025 import factorize


def test_factorize_zero_while_loop_never_entered():
    # Covers the case where the `while` condition on line 9 is False
    # immediately (i=2 > int(sqrt(0)+1) == 1) and the final `n > 1`
    # check is also False.
    assert factorize(0) == []


def test_factorize_one_returns_empty_list():
    # Loop body runs once via the else branch (i += 1); afterwards
    # n == 1 so the `if n > 1` branch is not taken.
    assert factorize(1) == []


def test_factorize_two():
    # Smallest prime: one True branch of `n % i == 0`, then n == 1.
    assert factorize(2) == [2]


def test_factorize_prime_covers_else_branch_and_final_append():
    # 97 is prime: the else branch (i += 1) is taken repeatedly until
    # the loop exits, and the trailing `if n > 1` branch appends it.
    assert factorize(97) == [97]


def test_factorize_prime_power_repeated_true_branch():
    # 8 = 2**3: the `n % i == 0` True branch is taken three times in a
    # row (append + n //= i), and the final `n > 1` check is False.
    assert factorize(8) == [2, 2, 2]


def test_factorize_composite_mixed_branches():
    # Exercises both the True branch (dividing) and the else branch
    # (incrementing i) within the same run, ending with n == 1.
    assert factorize(12) == [2, 2, 3]


def test_factorize_larger_composite():
    assert factorize(2 * 3 * 5 * 7 * 7 * 13) == [2, 3, 5, 7, 7, 13]


def test_factorize_square_of_large_prime():
    # 121 = 11**2: loop exits early (i grows past int(sqrt(11)+1)),
    # leaving n == 11 > 1, which must be appended by the final branch.
    assert factorize(121) == [11, 11]


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, []),
        (1, []),
        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (5, [5]),
        (6, [2, 3]),
        (9, [3, 3]),
        (25, [5, 5]),
        (100, [2, 2, 5, 5]),
        (360, [2, 2, 2, 3, 3, 5]),
        (1024, [2] * 10),
        (9973, [9973]),
    ],
)
def test_factorize_expected_factorizations(n, expected):
    assert factorize(n) == expected


@pytest.mark.parametrize(
    "n",
    [2, 3, 4, 6, 8, 12, 25, 49, 97, 121, 360, 1024, 2 * 3 * 5 * 7 * 7 * 13],
)
def test_factorize_postconditions(n):
    factors = factorize(n)
    # Every factor is a trial divisor >= 2 of the original n...
    assert all(f >= 2 and n % f == 0 for f in factors)
    # ...the factors are non-decreasing...
    assert factors == sorted(factors)
    # ...and their product reconstructs n exactly.
    product = 1
    for f in factors:
        product *= f
    assert product == n
