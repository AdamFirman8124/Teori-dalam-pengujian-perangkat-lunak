# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import types

from f059 import largest_prime_factor


def _find_nested(func, name):
    """Return a callable for the nested function ``name`` defined inside ``func``.

    ``is_prime`` is only ever invoked from the main loop with ``j >= 2``, so the
    ``k < 2`` early-return branch is unreachable through the public API.  The
    nested function's code object lives in ``func.__code__.co_consts``; rebuilding
    a function from it lets us execute that branch directly (same file, same
    line numbers, so coverage is credited correctly).
    """
    for const in func.__code__.co_consts:
        if isinstance(const, types.CodeType) and const.co_name == name:
            return types.FunctionType(const, func.__globals__, name)
    raise AssertionError(f"nested function {name!r} not found in {func.__name__}")


def test_largest_prime_factor_loop_never_entered():
    # n <= 1: range(2, n + 1) is empty, so the loop body (and is_prime)
    # never runs and the initial value 1 is returned.
    assert largest_prime_factor(1) == 1
    assert largest_prime_factor(0) == 1
    assert largest_prime_factor(-7) == 1


def test_largest_prime_factor_smallest_inputs():
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(3) == 3


def test_largest_prime_factor_composite_divisor_rejected():
    # Divisors that are not prime exercise the False branch of is_prime
    # inside the main loop (n % j == 0 holds but line 13 is skipped).
    assert largest_prime_factor(4) == 2   # j=4 divides 4 but is composite
    assert largest_prime_factor(8) == 2   # divisors 2, 4, 8 -> only 2 is prime
    assert largest_prime_factor(9) == 3   # j=9 divides 9 but is composite


def test_largest_prime_factor_typical_values():
    assert largest_prime_factor(6) == 3
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(21) == 7
    assert largest_prime_factor(100) == 5
    assert largest_prime_factor(13195) == 29


def test_nested_is_prime_all_branches():
    is_prime = _find_nested(largest_prime_factor, "is_prime")

    # k < 2 -> immediate False (the early-return branch)
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-3) is False

    # Smallest primes: range(2, k - 1) is empty -> loop runs zero times -> True
    assert is_prime(2) is True
    assert is_prime(3) is True

    # Composite: divisor found inside the loop -> early False
    assert is_prime(4) is False
    assert is_prime(9) is False
    assert is_prime(25) is False

    # Prime needing several loop iterations that complete without a divisor
    assert is_prime(5) is True
    assert is_prime(13) is True
    assert is_prime(97) is True
