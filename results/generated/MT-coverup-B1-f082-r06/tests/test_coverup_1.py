# file: project/f082/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

import pytest

from f082 import prime_length


def test_prime_length_empty_string():
    """len == 0 -> False (covers line 3, and the l == 0 branch of line 4)."""
    assert prime_length("") is False


def test_prime_length_single_char():
    """len == 1 -> False (covers the l == 1 branch of line 4)."""
    assert prime_length("a") is False


def test_prime_length_composite_length():
    """len == 4 is composite -> False via the loop (covers lines 6-8)."""
    assert prime_length("abcd") is False


def test_prime_length_prime_length():
    """len == 3 is prime -> True (covers lines 6-7 without hit, and line 9)."""
    assert prime_length("abc") is True


def test_prime_length_longer_prime():
    """len == 7 is prime -> True; loop runs fully without finding a divisor."""
    assert prime_length("abcdefg") is True


def test_prime_length_longer_composite():
    """len == 9 is composite (3*3) -> False via the loop."""
    assert prime_length("a" * 9) is False
