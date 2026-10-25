# file: project/f078/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f078 import hex_key


def test_hex_key_counts_prime_hex_digits():
    assert hex_key("2357BD") == 6


def test_hex_key_mixed_string():
    # primes: 2,3,5,7,B,D ; non-primes: 0,1,4,6,8,9,A,C,E,F
    assert hex_key("1234567890ABCDEF") == 6


def test_hex_key_empty_string():
    assert hex_key("") == 0


def test_hex_key_no_primes():
    assert hex_key("014689ACEF") == 0


def test_hex_key_single_prime():
    assert hex_key("B") == 1
