# file: project/f059/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8], [11, 12], [11, 14], [12, 11], [12, 13]]}

import types

import pytest

from f059 import largest_prime_factor


def _extract_is_prime():
    """Rebuild the nested ``is_prime`` helper from its code object.

    Through the public API ``is_prime`` is only ever invoked with ``j >= 2``,
    so the ``k < 2`` branch (line 5) is unreachable otherwise; invoking the
    nested function directly lets us cover every inner line and branch.
    """
    for const in largest_prime_factor.__code__.co_consts:
        if isinstance(const, types.CodeType) and const.co_name == "is_prime":
            return types.FunctionType(const, largest_prime_factor.__globals__)
    pytest.fail("nested 'is_prime' code object not found")


def test_composite_number_returns_largest_prime_factor():
    # Covers lines 3, 6, 9 (prime check), 10-14 (main loop, line 13 update).
    assert largest_prime_factor(15) == 5      # 3 * 5
    assert largest_prime_factor(13195) == 29  # 5 * 7 * 13 * 29
    assert largest_prime_factor(27) == 3      # 3 ** 3


def test_prime_input_returns_itself():
    # Covers the main loop with a single prime divisor (line 13, line 14).
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(13) == 13


def test_no_candidate_factors_returns_one():
    # Empty main loop (n <= 1): covers the loop-not-taken branch and line 14.
    assert largest_prime_factor(1) == 1
    assert largest_prime_factor(-7) == 1


def test_composite_divisors_are_skipped():
    # n % j == 0 but is_prime(j) is False: covers lines 7-8 and the
    # short-circuit branch of line 12, while prime divisors still hit line 13.
    assert largest_prime_factor(4) == 2
    assert largest_prime_factor(49) == 7


def test_is_prime_all_branches():
    is_prime = _extract_is_prime()
    assert is_prime(1) is False    # k < 2 -> line 5
    assert is_prime(0) is False    # k < 2 -> line 5
    assert is_prime(2) is True     # range(2, 1) empty -> line 9
    assert is_prime(3) is True     # range(2, 2) empty -> line 9
    assert is_prime(4) is False    # k % i == 0 -> lines 7-8
    assert is_prime(9) is False    # divisor found mid-loop -> lines 7-8
    assert is_prime(49) is False
    assert is_prime(17) is True    # loop completes without returning -> line 9
