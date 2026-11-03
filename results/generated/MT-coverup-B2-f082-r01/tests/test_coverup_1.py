# file: project/f082/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

import pytest

from f082 import prime_length


def test_prime_length_empty_string():
    """Covers lines 3-5 with l == 0."""
    assert prime_length("") is False


def test_prime_length_single_char():
    """Covers lines 3-5 with l == 1."""
    assert prime_length("a") is False


def test_prime_length_two_chars():
    """Covers lines 3, 4, 6, 9 (loop body skipped for l == 2)."""
    assert prime_length("ab") is True


def test_prime_length_three_chars():
    """Covers lines 3, 4, 6, 7 (non-divisible branch), 9."""
    assert prime_length("abc") is True


def test_prime_length_prime_length_string():
    """Covers lines 3, 4, 6, 7 (non-divisible branch), 9 with l == 7."""
    assert prime_length("abcdefg") is True


def test_prime_length_composite_length_string():
    """Covers lines 3, 4, 6, 7 (divisible branch), 8 with l == 4."""
    assert prime_length("abcd") is False


def test_prime_length_odd_composite_length_string():
    """Covers lines 3, 4, 6, 7 (divisible branch), 8 with l == 9."""
    assert prime_length("123456789") is False
