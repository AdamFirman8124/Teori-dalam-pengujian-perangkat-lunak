# file: project/f025/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}

import math

import pytest

from f025 import factorize


def test_factorize_composite_with_repeated_factors():
    """Covers loop entry, division branch (lines 10-12), loop exit, and
    the 'n > 1' False branch (line 16 not taken)."""
    result = factorize(12)
    assert result == [2, 2, 3]
    assert math.prod(result) == 12
    assert result == sorted(result)
    assert all(f > 1 for f in result)


def test_factorize_prime():
    """Covers the else branch (line 14) and the 'n > 1' True branch
    (lines 16-17) where the remaining prime is appended."""
    result = factorize(13)
    assert result == [13]
    assert math.prod(result) == 13


def test_factorize_two():
    """Smallest prime: loop body runs once, then n becomes 1."""
    result = factorize(2)
    assert result == [2]
    assert math.prod(result) == 2


def test_factorize_perfect_square():
    """Same prime divided out repeatedly; final n is 1 (line 16 False)."""
    result = factorize(4)
    assert result == [2, 2]
    assert math.prod(result) == 4


def test_factorize_one_returns_empty():
    """n = 1: loop entered but no divisor found, no leftover factor."""
    assert factorize(1) == []


def test_factorize_large_composite():
    """Multiple distinct primes; exercises both branches of line 10
    several times and fully divides n (line 16 False)."""
    result = factorize(100)
    assert result == [2, 2, 5, 5]
    assert math.prod(result) == 100


def test_factorize_leftover_large_prime():
    """After the loop exits early (i exceeds sqrt(remaining)+1), the
    leftover prime 5 is appended via lines 16-17."""
    result = factorize(360)
    assert result == [2, 2, 2, 3, 3, 5]
    assert math.prod(result) == 360


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, [2]),
        (3, [3]),
        (4, [2, 2]),
        (6, [2, 3]),
        (9, [3, 3]),
        (15, [3, 5]),
        (17, [17]),
        (49, [7, 7]),
        (97, [97]),
        (128, [2] * 7),
    ],
)
def test_factorize_parametrized(n, expected):
    result = factorize(n)
    assert result == expected
    assert math.prod(result) == n
    assert result == sorted(result)
