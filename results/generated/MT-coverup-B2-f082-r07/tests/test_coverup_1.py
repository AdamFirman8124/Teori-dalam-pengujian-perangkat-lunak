# file: project/f082/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

from f082 import prime_length


def test_prime_length_rejects_empty_and_single_character_strings():
    assert prime_length("") is False
    assert prime_length("a") is False


def test_prime_length_accepts_prime_lengths():
    assert prime_length("ab") is True
    assert prime_length("abc") is True


def test_prime_length_rejects_composite_length():
    assert prime_length("abcd") is False
