# file: project/f078/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

from f078 import hex_key


def test_hex_key_empty():
    assert hex_key("") == 0


def test_hex_key_no_primes():
    assert hex_key("014689ACEF018") == 0


def test_hex_key_all_primes():
    assert hex_key("2357BD") == 6


def test_hex_key_mixed():
    assert hex_key("0123456789ABCDEF") == 6
