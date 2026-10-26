# file: project/f082/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

import pytest

from f082 import prime_length


def test_prime_length_empty_string():
    """Covers lines 3-5: l == 0 branch returns False."""
    assert prime_length("") is False


def test_prime_length_single_char():
    """Covers lines 3-5: l == 1 branch returns False."""
    assert prime_length("a") is False


def test_prime_length_composite_length():
    """Covers lines 6-8: loop finds a divisor (l % i == 0) and returns False."""
    assert prime_length("abcd") is False  # length 4, divisible by 2


def test_prime_length_prime_length():
    """Covers lines 6-9: loop completes without finding a divisor, returns True."""
    assert prime_length("abc") is True  # length 3, prime
