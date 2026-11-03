# file: project/f082/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

import pytest

from f082 import prime_length


def test_prime_length_empty_string():
    # Covers lines 3, 4 (l == 0 branch True) and 5
    assert prime_length("") is False


def test_prime_length_single_char():
    # Covers lines 3, 4 (l == 1 branch True) and 5
    assert prime_length("a") is False


def test_prime_length_two_chars():
    # Covers lines 3, 4 (branch False), 6 (loop body never runs) and 9
    assert prime_length("ab") is True


def test_prime_length_prime_length_string():
    # Covers lines 3, 4 (branch False), 6, 7 (l % i != 0) and 9
    assert prime_length("abc") is True
    assert prime_length("hello") is True  # len 5 is prime


def test_prime_length_composite_length_string():
    # Covers lines 3, 4 (branch False), 6, 7 (l % i == 0) and 8
    assert prime_length("abcd") is False
    assert prime_length("a" * 6) is False
