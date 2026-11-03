# file: project/f025/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}

import math
from typing import List

import pytest

from f025 import factorize


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, []),            # while-condition false immediately; final n > 1 false
        (1, []),            # loop body runs once (i += 1 branch); final n > 1 false
        (2, [2]),           # divisible branch (append + n //= i); n > 1 false after division
        (3, [3]),           # non-divisible branch, loop exhausts, remainder appended
        (4, [2, 2]),        # repeated factor
        (6, [2, 3]),        # divisible, then non-divisible, then trailing prime
        (9, [3, 3]),        # several i += 1 iterations before first hit
        (12, [2, 2, 3]),
        (97, [97]),         # large prime: loop exhausts without dividing
        (100, [2, 2, 5, 5]),
        (2 * 3 * 5 * 7 * 11, [2, 3, 5, 7, 11]),
    ],
)
def test_factorize_known_values(n: int, expected: List[int]) -> None:
    assert factorize(n) == expected


@pytest.mark.parametrize("n", list(range(1, 500)))
def test_factorize_reconstructs_original_number(n: int) -> None:
    factors = factorize(n)
    product = 1
    for f in factors:
        product *= f
    assert product == n


@pytest.mark.parametrize("n", list(range(2, 500)))
def test_factorize_returns_sorted_primes(n: int) -> None:
    factors = factorize(n)
    assert factors == sorted(factors)
    for f in factors:
        assert all(f % d != 0 for d in range(2, int(math.sqrt(f)) + 1))
