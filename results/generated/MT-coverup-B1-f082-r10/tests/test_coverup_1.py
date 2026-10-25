# file: project/f082/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

from f082 import prime_length


def test_prime_length_empty_string_returns_false():
    assert prime_length("") is False


def test_prime_length_single_character_string_returns_false():
    assert prime_length("a") is False


def test_prime_length_composite_length_returns_false():
    assert prime_length("abcd") is False


def test_prime_length_prime_length_returns_true():
    assert prime_length("abcde") is True
