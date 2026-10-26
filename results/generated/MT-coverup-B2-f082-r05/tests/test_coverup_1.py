# file: project/f082/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

import pytest

from f082 import prime_length


def test_prime_length_empty_string():
    assert prime_length("") is False


def test_prime_length_single_char():
    assert prime_length("a") is False


def test_prime_length_two_chars_is_prime():
    assert prime_length("ab") is True


def test_prime_length_composite_even():
    assert prime_length("abcd") is False


def test_prime_length_composite_odd():
    assert prime_length("abcdefghi") is False


def test_prime_length_prime_odd():
    assert prime_length("abcdefg") is True
