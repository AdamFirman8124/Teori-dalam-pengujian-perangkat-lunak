# file: project/f078/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f078 import hex_key


def test_hex_key_counts_prime_hex_digits():
    assert hex_key("AB") == 1          # A not prime, B prime
    assert hex_key("1077E") == 2       # 7 and 7 are prime
    assert hex_key("ABED1A33") == 4    # B, D, 3, 3
    assert hex_key("123456789ABCDEF0") == 6  # 2, 3, 5, 7, B, D
    assert hex_key("2020") == 2        # two 2s
    assert hex_key("") == 0            # loop body never runs
    assert hex_key("01489ACEF") == 0   # no prime digits at all
