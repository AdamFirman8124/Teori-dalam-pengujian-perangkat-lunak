# file: project/f078/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f078 import hex_key


def test_hex_key_empty_string():
    """An empty input contains no digits, so the loop body never runs and total stays 0."""
    assert hex_key("") == 0


def test_hex_key_no_primes():
    """Hex digits that are not prime (0, 1, 4, 6, 8, 9, A, C, E, F) count 0."""
    assert hex_key("014689ACEF") == 0


def test_hex_key_all_primes():
    """Every digit is a hexadecimal prime, so total equals the length."""
    num = "2357BD"
    assert hex_key(num) == len(num) == 6


def test_hex_key_mixed():
    """A mixed string counts only the prime hex digits."""
    assert hex_key("AB") == 1  # A not prime, B prime
    assert hex_key("107") == 1  # 1 no, 0 no, 7 yes
    assert hex_key("FF") == 0
    assert hex_key("2D") == 2
    assert hex_key("FE") == 0
    assert hex_key("FD") == 1
    assert hex_key("ABED") == 2  # B and D are prime


def test_hex_key_huahua_example():
    """Classic HumanEval examples for hex_key."""
    assert hex_key("AB") == 1
    assert hex_key("1077E") == 2
    assert hex_key("ABED1A33") == 4
    assert hex_key("123456789ABCDEF0") == 6
    assert hex_key("2020") == 2


def test_hex_key_single_prime_digit():
    """Each individual prime digit yields 1 and exercise each branch of the membership test."""
    for d in ("2", "3", "5", "7", "B", "D"):
        assert hex_key(d) == 1
    for d in ("0", "1", "4", "6", "8", "9", "A", "C", "E", "F"):
        assert hex_key(d) == 0
