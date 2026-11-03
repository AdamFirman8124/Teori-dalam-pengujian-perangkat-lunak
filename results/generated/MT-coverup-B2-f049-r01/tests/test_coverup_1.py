# file: project/f049/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

import pytest

from f049 import modp


def test_modp_positive_exponent():
    """2^3 mod 5 == 8 mod 5 == 3; exercises the loop body (lines 4-5)."""
    assert modp(3, 5) == 3
    assert modp(3, 5) == pow(2, 3, 5)


def test_modp_zero_exponent():
    """2^0 == 1, so the loop body never runs but lines 3 and 6 execute."""
    assert modp(0, 13) == 1


def test_modp_larger_values():
    """2^10 mod 13 == 1024 mod 13 == 10."""
    assert modp(10, 13) == 10
    assert modp(10, 13) == pow(2, 10, 13)


def test_modp_wraps_multiple_times():
    """Result is always in [0, p) even when the accumulator wraps often."""
    result = modp(100, 7)
    assert result == pow(2, 100, 7)
    assert 0 <= result < 7


def test_modp_negative_n():
    """range(n) for n < 0 is empty, so modp returns 1."""
    assert modp(-5, 11) == 1


def test_modp_matches_builtin_pow_many_cases():
    """Property-style check against the reference implementation."""
    for n in range(0, 20):
        for p in (2, 3, 5, 7, 101):
            assert modp(n, p) == pow(2, n, p) % p
