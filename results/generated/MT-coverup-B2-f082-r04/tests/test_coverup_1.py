# file: project/f082/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

import pytest

from f082 import prime_length


def test_prime_length_empty_string():
    """Covers lines 3-5 via the l == 0 branch."""
    assert prime_length("") is False


def test_prime_length_single_char():
    """Covers lines 3-5 via the l == 1 branch."""
    assert prime_length("a") is False


def test_prime_length_two_chars():
    """l == 2: loop body (range(2, 2)) never executes, covers line 9."""
    assert prime_length("ab") is True


def test_prime_length_composite():
    """l == 4: loop finds divisor 2, covers lines 6-8."""
    assert prime_length("abcd") is False


def test_prime_length_prime():
    """l == 3: loop runs, no divisor found, covers lines 6, 7 and 9."""
    assert prime_length("abc") is True


def test_prime_length_larger_prime():
    """l == 7: exercises multiple loop iterations before returning True."""
    assert prime_length("1234567") is True


def test_prime_length_larger_composite():
    """l == 9: divisor found on a later iteration, covers lines 6-8 again."""
    assert prime_length("123456789") is False
