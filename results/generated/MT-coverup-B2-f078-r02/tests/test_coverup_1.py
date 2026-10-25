# file: project/f078/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

from f078 import hex_key


def test_hex_key_empty_string():
    assert hex_key("") == 0


def test_hex_key_all_primes():
    assert hex_key("2357BD") == 6


def test_hex_key_no_primes():
    assert hex_key("014689ACEF") == 0


def test_hex_key_mixed_prime_and_non_prime():
    assert hex_key("2A3F5") == 3
    assert hex_key("A2") == 1
    assert hex_key("2A") == 1


def test_hex_key_single_characters():
    assert hex_key("2") == 1
    assert hex_key("B") == 1
    assert hex_key("D") == 1
    assert hex_key("A") == 0
    assert hex_key("0") == 0


def test_hex_key_lowercase_not_counted():
    assert hex_key("bd") == 0
    assert hex_key("BD") == 2
