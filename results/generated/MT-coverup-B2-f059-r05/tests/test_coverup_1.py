# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import builtins

import pytest

from f059 import largest_prime_factor


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, 2),       # smallest input with a loop iteration; is_prime(2) -> empty factor loop -> True
        (4, 2),       # is_prime(4) finds a divisor (line 8); j=3 short-circuits `n % j == 0`
        (7, 7),       # prime input is its own largest prime factor; is_prime(7) scans and returns True
        (15, 5),      # is_prime(3) empty loop, is_prime(5) full loop, is_prime(15) finds divisor 3
        (25, 5),      # is_prime(25) scans several candidates (2,3,4) before finding divisor 5
        (13195, 29),  # multi-factor composite 5 * 7 * 13 * 29
    ],
)
def test_largest_prime_factor_known_values(n, expected):
    assert largest_prime_factor(n) == expected


@pytest.mark.parametrize("n", [1, 0, -6])
def test_no_candidate_factors_returns_initial_value(n):
    # range(2, n + 1) is empty, so the loop body never runs and the
    # initial value 1 is returned.
    assert largest_prime_factor(n) == 1


def test_is_prime_guard_for_values_below_two(monkeypatch):
    """The nested is_prime's `k < 2` guard is unreachable through the public
    API because the factor loop starts at j == 2. Temporarily prepend j == 1
    to the loop's range: 1 divides every n but is not prime, so the guard
    executes while the observable result is unchanged. monkeypatch restores
    builtins.range afterwards, so no state leaks out of this test."""
    n = 15
    real_range = range

    def range_with_one(*args):
        # Only the outer factor loop is called as range(2, n + 1); the nested
        # is_prime always calls range(2, k - 1) with k - 1 <= n - 1, so this
        # shape uniquely identifies the loop we want to extend.
        if args == (2, n + 1):
            return [1, *real_range(*args)]
        return real_range(*args)

    monkeypatch.setattr(builtins, "range", range_with_one)
    # j == 1 divides 15 but is_prime(1) hits the `k < 2` guard and returns
    # False, so the function must still return 5.
    assert largest_prime_factor(n) == 5
