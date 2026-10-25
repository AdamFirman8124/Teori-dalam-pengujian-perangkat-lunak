# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import types
from f059 import largest_prime_factor


def test_no_prime_factors_returns_one():
    assert largest_prime_factor(1) == 1
    assert largest_prime_factor(0) == 1
    assert largest_prime_factor(-5) == 1


def test_small_primes_empty_inner_loop():
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(3) == 3


def test_prime_requires_full_inner_scan():
    assert largest_prime_factor(13) == 13
    assert largest_prime_factor(17) == 17


def test_composite_with_nonprime_divisor():
    assert largest_prime_factor(4) == 2
    assert largest_prime_factor(12) == 3
    assert largest_prime_factor(30) == 5


def test_delayed_composite_detection_in_is_prime():
    assert largest_prime_factor(9) == 3
    assert largest_prime_factor(27) == 3
    assert largest_prime_factor(49) == 7


def test_inner_is_prime_k_less_than_two():
    inner_code = next(
        c for c in largest_prime_factor.__code__.co_consts
        if isinstance(c, types.CodeType) and c.co_name == "is_prime"
    )
    is_prime = types.FunctionType(inner_code, {})
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(-10) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(9) is False
