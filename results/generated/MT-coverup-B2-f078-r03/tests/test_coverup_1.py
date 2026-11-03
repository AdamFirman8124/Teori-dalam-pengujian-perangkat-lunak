# file: project/f078/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f078 import hex_key


def test_hex_key_all_prime_digits():
    """All characters are prime hex digits; every loop iteration takes the True branch."""
    assert hex_key("2357BD") == 6


def test_hex_key_no_prime_digits():
    """No characters are prime hex digits; every loop iteration takes the False branch."""
    assert hex_key("014689ACEF") == 0


def test_hex_key_mixed_digits():
    """A mix of prime and non-prime hex digits counts only the primes."""
    assert hex_key("AB") == 1
    assert hex_key("1077S") == 2
    assert hex_key("0202") == 2
    assert hex_key("FF") == 0


def test_hex_key_empty_string():
    """An empty string skips the loop body entirely and returns 0."""
    assert hex_key("") == 0


def test_hex_key_single_prime_digit():
    """A single prime digit exercises one full loop pass."""
    assert hex_key("D") == 1


def test_hex_key_longer_example():
    """A longer mixed example verifies the running total."""
    assert hex_key("123456789ABCDEF0") == 6
