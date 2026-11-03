# file: project/f075/__init__.py:1-19
# asked: {"lines": [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}

import pytest

from f075 import is_multiply_prime


@pytest.mark.parametrize(
    "a, factors",
    [
        (8, (2, 2, 2)),
        (12, (2, 2, 3)),
        (18, (2, 3, 3)),
        (20, (2, 2, 5)),
        (27, (3, 3, 3)),
        (28, (2, 2, 7)),
        (30, (2, 3, 5)),
        (98, (2, 7, 7)),
        (105, (3, 5, 7)),
        (125, (5, 5, 5)),
        # Largest value reachable by the loops: 97 * 97 * 97.  Reaching it
        # forces the i/j/k loops to run far enough to skip many composite
        # values via the `continue` branches (lines 13, 15, 17).
        (912673, (97, 97, 97)),
    ],
)
def test_is_multiply_prime_true(a, factors):
    # Sanity-check the test data itself: a really is a product of three primes.
    assert factors[0] * factors[1] * factors[2] == a
    # Postcondition: the function recognizes a as a product of three primes.
    assert is_multiply_prime(a) is True


@pytest.mark.parametrize(
    "a",
    [
        1,       # no prime factors at all; drives all three loops to exhaustion
        0,       # zero
        -30,     # negative
        2,       # a single prime
        6,       # product of only two primes (2 * 3)
        26,      # product of only two primes (2 * 13)
        64,      # 2**6 -> six prime factors, not three
        1000,    # 2**3 * 5**3 -> six prime factors, not three
        912674,  # strictly greater than the largest reachable product (97**3)
    ],
)
def test_is_multiply_prime_false(a):
    # Postcondition: none of these values is a product of exactly three primes.
    # The `1` case in particular executes every loop iteration, covering the
    # `continue` branches for composite i, j and k, and the final
    # `return False` (line 19).
    assert is_multiply_prime(a) is False
