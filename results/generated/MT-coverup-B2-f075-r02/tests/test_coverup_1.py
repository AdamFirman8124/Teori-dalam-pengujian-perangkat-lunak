# file: project/f075/__init__.py:1-19
# asked: {"lines": [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}

import pytest

from f075 import is_multiply_prime


@pytest.mark.parametrize(
    "a, expected",
    [
        # Products of exactly three primes -> True (hits line 18: return True)
        (30, True),        # 2 * 3 * 5
        (8, True),         # 2 * 2 * 2 (repeated prime factors)
        (12, True),        # 2 * 2 * 3
        (18, True),        # 2 * 3 * 3
        (105, True),       # 3 * 5 * 7
        (912673, True),    # 97 * 97 * 97 (largest product reachable in range)
        # Not a product of exactly three primes -> False (hits line 19: return False)
        (1, False),        # no prime factors at all
        (0, False),
        (-30, False),      # negative input can never match i*j*k (all positive)
        (5, False),        # a prime itself, not a product of three primes
        (16, False),       # 2^2*2^2 -> product of four primes
        (404, False),      # 2 * 2 * 101, but 101 is outside the loop range (2..100)
    ],
)
def test_is_multiply_prime(a, expected):
    """is_multiply_prime must return True iff a is a product of exactly
    three (not necessarily distinct) primes, each less than 100."""
    result = is_multiply_prime(a)
    assert result == expected
    assert isinstance(result, bool)


def test_is_multiply_prime_returns_true_for_known_triple():
    # Exercises the full nested-loop machinery: is_prime returning True for
    # primes (2, 3, 5), the 'continue' branches for composite i/j/k values
    # (e.g. 4, 6, 8, 9), and the early 'return True' on line 18.
    assert is_multiply_prime(2 * 3 * 5) is True


def test_is_multiply_prime_returns_false_when_no_triple_matches():
    # Exercises the 'return False' fall-through on line 19 after all loops
    # complete without a match, including the 'continue' branches taken for
    # every composite value of i, j and k.
    assert is_multiply_prime(1) is False
    assert is_multiply_prime(2 * 2 * 2 * 2) is False
