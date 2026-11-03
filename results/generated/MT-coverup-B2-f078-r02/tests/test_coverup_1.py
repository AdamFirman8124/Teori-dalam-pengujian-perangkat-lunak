# file: project/f078/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f078 import hex_key


def test_hex_key_all_prime_digits():
    """Every character is a prime hex digit: the if-branch (line 7) executes."""
    assert hex_key("2357BD") == 6


def test_hex_key_no_prime_digits():
    """No character is a prime hex digit: the if-condition is evaluated but never true."""
    assert hex_key("014689ACEF") == 0


def test_hex_key_mixed_string():
    """Mixed string exercises both branches of the if on different iterations."""
    assert hex_key("123456789ABCDEF0") == 6
    assert hex_key("AB") == 1
    assert hex_key("1077E") == 2
    assert hex_key("ABED1A33") == 4
    assert hex_key("2020") == 2


def test_hex_key_empty_string():
    """Empty input: the for-loop body never executes (loop branch not taken)."""
    assert hex_key("") == 0


def test_hex_key_single_characters():
    """Single-character inputs cover loop entry with one iteration."""
    assert hex_key("B") == 1
    assert hex_key("D") == 1
    assert hex_key("A") == 0
    assert hex_key("F") == 0


def test_hex_key_lowercase_not_counted():
    """Lowercase letters are not in the primes tuple, so the if is False."""
    assert hex_key("b") == 0
    assert hex_key("bd") == 0
