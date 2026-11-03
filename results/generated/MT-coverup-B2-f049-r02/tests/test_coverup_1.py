# file: project/f049/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

import pytest

from f049 import modp


def test_modp_zero_iterations():
    """n = 0 skips the loop body entirely (covers lines 3, 4, 6)."""
    assert modp(0, 101) == 1


def test_modp_basic():
    """n > 0 executes the loop body (covers line 5)."""
    assert modp(3, 5) == 3          # 2**3 = 8, 8 % 5 == 3
    assert modp(3, 11) == 8         # 2**3 = 8, 8 % 11 == 8
    assert modp(10, 101) == 14      # 2**10 = 1024, 1024 % 101 == 14


def test_modp_matches_direct_power():
    """Result equals 2**n % p for several (n, p) pairs."""
    for n, p in [(1, 3), (2, 7), (5, 13), (20, 1000003), (100, 101)]:
        assert modp(n, p) == pow(2, n, p)


def test_modp_fermat():
    """2**100 mod 101 == 1 by Fermat's little theorem (101 is prime)."""
    assert modp(100, 101) == 1
