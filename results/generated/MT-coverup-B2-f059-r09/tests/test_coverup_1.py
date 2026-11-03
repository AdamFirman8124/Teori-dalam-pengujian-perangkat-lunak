# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import types

import pytest

from f059 import largest_prime_factor


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (13195, 29),  # 13195 = 5 * 7 * 13 * 29: several prime factors, max() updates (line 13)
        (2048, 2),    # 2048 = 2 ** 11: composite divisors drive is_prime's inner loop (lines 7-8)
        (4, 2),       # smallest composite divisor: is_prime(4) returns False via k % i == 0
        (21, 7),      # 21 = 3 * 7
        (13, 13),     # prime n is its own largest prime factor (is_prime inner loop exhausts)
        (3, 3),       # is_prime(3): inner loop range(2, 2) is empty -> True
        (2, 2),       # is_prime(2): inner loop range(2, 1) is empty -> True
        (1, 1),       # degenerate input: the j-loop body never runs (empty range branch)
        (0, 1),       # degenerate input: range(2, n + 1) is empty
        (-10, 1),     # degenerate input: range(2, n + 1) is empty
    ],
)
def test_largest_prime_factor(n, expected):
    # largest_prime_factor is a pure function: it mutates no state, so no
    # monkeypatching/cleanup is required here.
    assert largest_prime_factor(n) == expected


def test_largest_prime_factor_short_circuits_is_prime():
    # n % j != 0 must short-circuit the `and is_prime(j)` check (line 12);
    # 3 does not divide 13195, yet 3 is prime, so only the first condition
    # being False can produce the correct result below.
    assert largest_prime_factor(13195) == 29
    # n % j == 0 with a composite j must NOT update `largest` (line 12 False
    # branch): 4 divides 12 but the answer must be 3, not 4.
    assert largest_prime_factor(12) == 3


def test_nested_is_prime_k_below_two():
    """Cover the ``k < 2`` early return of the nested ``is_prime``.

    Through ``largest_prime_factor`` itself, ``is_prime`` is only ever called
    with ``j >= 2`` (the outer loop starts at 2), so the ``k < 2`` branch is
    unreachable from the public API.  The nested function is reconstructed
    from its code object (it uses no closures, only builtins) and exercised
    directly.  Nothing is mutated, so no cleanup is required.
    """
    code = next(
        const
        for const in largest_prime_factor.__code__.co_consts
        if isinstance(const, types.CodeType) and const.co_name == "is_prime"
    )
    is_prime = types.FunctionType(code, largest_prime_factor.__globals__)

    # k < 2 -> early False (the otherwise unreachable line/branch).
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-3) is False
    # Sanity checks on the reachable domain: primes and composites.
    assert is_prime(2) is True
    assert is_prime(5) is True
    assert is_prime(9) is False
