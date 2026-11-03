# file: project/f049/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

"""Tests for f049.modp, which computes 2**n % p via repeated doubling.

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching or fixture-based cleanup is required to avoid state pollution.
"""

import pytest

from f049 import modp


@pytest.mark.parametrize(
    "n, p, expected",
    [
        # n == 0: line 3 and 6 execute, loop body (lines 4-5) does not.
        (0, 101, 1),
        # Loop body executes exactly once.
        (1, 101, 2),
        # Loop body executes multiple times.
        (3, 11, 8),
        (10, 101, 14),  # 1024 % 101 == 14
        # Modulus of 1 forces the modulo reduction to 0.
        (5, 1, 0),
        # Negative n: range(n) is empty, so the loop body never runs.
        (-3, 7, 1),
        # Fermat's little theorem: 101 is prime, so 2**100 % 101 == 1.
        (100, 101, 1),
    ],
)
def test_modp_known_values(n, p, expected):
    """Execute all lines 3-6 and verify postconditions."""
    result = modp(n, p)
    assert result == expected
    # Postcondition: result is always a valid residue modulo p (or 1 when
    # the loop never runs and p > 1).
    if p > 1:
        assert 0 <= result < p


def test_modp_matches_builtin_pow():
    """Cross-check the loop-based implementation against pow(2, n, p)."""
    for n in range(0, 33):
        for p in (2, 3, 5, 7, 101, 997, 10**9 + 7):
            assert modp(n, p) == pow(2, n, p)
