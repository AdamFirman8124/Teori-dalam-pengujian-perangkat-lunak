# file: project/f082/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

from f082 import prime_length


def test_prime_length_returns_false_for_empty_string():
    assert prime_length("") is False


def test_prime_length_returns_false_for_single_character_string():
    assert prime_length("a") is False


def test_prime_length_returns_false_for_composite_length():
    assert prime_length("abcd") is False


def test_prime_length_returns_true_for_prime_length():
    assert prime_length("ab") is True
    assert prime_length("abc") is True
