# file: project/f078/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f078 import hex_key


def test_hex_key_all_prime_digits():
    # Covers lines 3-8, including the True branch of the membership test
    # and the increment on line 7.
    assert hex_key("2357BD") == 6


def test_hex_key_no_prime_digits():
    # Covers the False branch of the membership test on line 6.
    assert hex_key("014689ACEF") == 0


def test_hex_key_mixed_digits():
    # Covers both branches of the membership test within one call.
    assert hex_key("AB") == 1      # 'A' is not prime, 'B' is
    assert hex_key("2020") == 2    # '2' prime, '0' not
    assert hex_key("6999") == 0    # '6' and '9' are not prime hex digits
    assert hex_key("2A3D4") == 3   # '2', '3', 'D' are prime


def test_hex_key_empty_string():
    # Covers the branch where the loop body never executes.
    assert hex_key("") == 0


def test_hex_key_longer_example():
    # Classic examples: "1077E" -> 2 primes ('7','7'),
    # "AED" -> 1 prime ('D'), "123456789ABCDEF0" -> 6 primes.
    assert hex_key("1077E") == 2
    assert hex_key("AED") == 1
    assert hex_key("123456789ABCDEF0") == 6
