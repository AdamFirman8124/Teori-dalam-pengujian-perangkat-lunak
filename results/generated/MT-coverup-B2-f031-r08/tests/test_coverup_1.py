# file: project/f031/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f031 import is_prime


def test_is_prime_returns_false_for_n_less_than_two():
    """Covers line 3 (condition true) and line 4 (early return)."""
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-7) is False


def test_is_prime_returns_false_for_composite_numbers():
    """Covers lines 5-7: loop body finds a divisor and returns False."""
    assert is_prime(4) is False   # range(2, 3) -> k=2 divides 4
    assert is_prime(9) is False   # k=3 divides 9
    assert is_prime(15) is False  # k=3 divides 15


def test_is_prime_returns_true_for_two_and_three():
    """Covers line 8 via the branch where the loop body never executes."""
    assert is_prime(2) is True    # range(2, 1) is empty
    assert is_prime(3) is True    # range(2, 2) is empty


def test_is_prime_returns_true_for_primes():
    """Covers line 8 via the branch where the loop completes without a divisor."""
    assert is_prime(5) is True    # range(2, 4): 5 % 2 != 0, 5 % 3 != 0
    assert is_prime(7) is True    # range(2, 6): no divisor found
    assert is_prime(11) is True   # range(2, 10): no divisor found
