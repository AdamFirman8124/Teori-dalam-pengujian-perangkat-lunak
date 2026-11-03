# file: project/f075/__init__.py:1-19
# asked: {"lines": [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [12, 13], [12, 19], [13, 13], [13, 14], [14, 12], [14, 15], [15, 15], [15, 16], [16, 14], [16, 17], [17, 17], [17, 18], [18, 16], [18, 18]]}

"""Tests for f075.is_multiply_prime.

The function is pure (no I/O, no module-level state), so no monkeypatching
or teardown is required; each test leaves no state behind.
"""

from f075 import is_multiply_prime


def test_is_multiply_prime_true_distinct_primes():
    """30 = 2 * 3 * 5, so it is a product of three primes.

    Covers: is_prime returning True (line 7) and False (line 6, hit for
    composite candidates such as 4), the 'continue' branches (lines 13,
    15, 17), and the early 'return True' (line 18).
    """
    assert is_multiply_prime(30) is True


def test_is_multiply_prime_true_repeated_prime():
    """8 = 2 * 2 * 2, so it is a product of three primes."""
    assert is_multiply_prime(8) is True


def test_is_multiply_prime_false_exhausts_search():
    """1 cannot be written as i*j*k with 2 <= i, j, k <= 100, so the
    entire triple loop runs and the final 'return False' (line 19) is hit.
    """
    assert is_multiply_prime(1) is False


def test_is_multiply_prime_false_out_of_range_factor():
    """404 = 2 * 2 * 101, but 101 is outside the searched range, so no
    triple (i, j, k) with 2 <= i, j, k <= 100 multiplies to 404.
    """
    assert is_multiply_prime(404) is False
