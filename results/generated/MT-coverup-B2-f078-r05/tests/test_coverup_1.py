# file: project/f078/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f078 import hex_key


def test_hex_key_all_prime_digits():
    """Every character is a prime hex digit; covers lines 3-8 including the
    True branch of the membership test (line 7 executes)."""
    assert hex_key("2357BD") == 6


def test_hex_key_no_prime_digits():
    """No character is a prime hex digit; covers the False branch of the
    membership test on line 6."""
    assert hex_key("014689ACEF") == 0


def test_hex_key_mixed_digits():
    """A mix of prime and non-prime hex digits; exercises both branches of
    the membership test within a single loop."""
    assert hex_key("2020") == 2
    assert hex_key("AB") == 1
    assert hex_key("1077S") == 2  # '7' twice; '1', '0', 'S' are not prime


def test_hex_key_empty_string():
    """Empty input: loop body never executes, still returns 0 (line 8)."""
    assert hex_key("") == 0


def test_hex_key_counts_each_occurrence():
    """Repeated prime digits are each counted individually."""
    assert hex_key("BBBB") == 4
    assert hex_key("DD22") == 4
    assert hex_key("FFFF") == 0
