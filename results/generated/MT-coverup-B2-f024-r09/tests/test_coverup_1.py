# file: project/f024/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 0], [3, 4], [4, 3], [4, 5]]}

import pytest

from f024 import largest_divisor


def test_largest_divisor_two_returns_one():
    # n=2 -> loop runs once with i=1, hits the return on line 5
    assert largest_divisor(2) == 1


def test_largest_divisor_skips_non_divisors():
    # n=4 -> i=3 fails the modulo check (False branch), i=2 returns
    assert largest_divisor(4) == 2


def test_largest_divisor_prime_returns_one():
    assert largest_divisor(7) == 1


def test_largest_divisor_composite_postconditions():
    n = 100
    result = largest_divisor(n)
    assert result == 50
    assert n % result == 0
    assert result < n
    assert all(n % d != 0 for d in range(result + 1, n))


def test_largest_divisor_zero_returns_none():
    # empty range: loop body never runs, implicit None
    assert largest_divisor(0) is None


def test_largest_divisor_negative_returns_none():
    assert largest_divisor(-5) is None


def test_largest_divisor_one_raises_zero_division():
    # range(1) -> [0], so n % 0 raises
    with pytest.raises(ZeroDivisionError):
        largest_divisor(1)
