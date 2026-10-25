# file: project/f025/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}

import pytest

from f025 import factorize


def _assert_factorization(n, expected):
    result = factorize(n)
    assert result == expected
    # postconditions: product reconstructs n, factors are prime and non-decreasing
    product = 1
    for f in result:
        product *= f
        assert f >= 2
        assert all(f % d for d in range(2, int(f ** 0.5) + 1))
    assert product == n
    assert result == sorted(result)


def test_factorize_composite_with_repeated_factor():
    # covers lines 6-18: import, loop, if-branch (append + n //= i), else-branch, final n > 1
    _assert_factorization(12, [2, 2, 3])


def test_factorize_one_skips_final_append():
    # covers the False branch of `if n > 1` (line 16)
    _assert_factorization(1, [])


def test_factorize_prime_returns_itself():
    # loop never divides, final append executes
    _assert_factorization(97, [97])


def test_factorize_power_of_two():
    # repeated if-branch without else-branch
    _assert_factorization(8, [2, 2, 2])


def test_factorize_two():
    _assert_factorization(2, [2])


def test_factorize_large_semiprime():
    _assert_factorization(10403, [101, 103])
