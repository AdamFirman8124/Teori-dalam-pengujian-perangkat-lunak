# file: project/f025/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14], [16, 17], [16, 18]]}

import pytest

from f025 import factorize


def test_factorize_composite_with_repeated_factors():
    # Exercises the loop body, the n % i == 0 branch (lines 10-12),
    # and the final n > 1 branch (lines 16-17).
    assert factorize(360) == [2, 2, 2, 3, 3, 5]
    # Postcondition: product of factors reconstructs the input.
    result = 1
    for f in factorize(360):
        result *= f
    assert result == 360


def test_factorize_prime():
    # A prime input: loop finds no divisor, else-branch (line 14) runs,
    # and the trailing n > 1 branch appends n (lines 16-18).
    assert factorize(13) == [13]


def test_factorize_large_prime():
    # Forces the while condition (line 9) to be evaluated many times
    # via the else branch before exiting.
    assert factorize(97) == [97]


def test_factorize_one():
    # n = 1: loop never runs, n > 1 is False, returns empty list (line 18).
    assert factorize(1) == []


def test_factorize_two():
    # Smallest case entering the loop: 2 <= int(sqrt(2) + 1) is True,
    # 2 % 2 == 0 so n becomes 1, loop exits, n > 1 is False.
    assert factorize(2) == [2]


def test_factorize_square_of_prime():
    # Ensures the same divisor is consumed twice (append + //= path).
    assert factorize(49) == [7, 7]


def test_factorize_product_of_two_primes():
    # Mixed branches: first divisor found, then i incremented past it.
    assert factorize(15) == [3, 5]
