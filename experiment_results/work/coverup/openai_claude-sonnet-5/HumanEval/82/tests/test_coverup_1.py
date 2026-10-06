# file: script_82.py:1-16
# asked: {"lines": [10, 11, 12, 13, 14, 15, 16], "branches": [[11, 12], [11, 13], [13, 14], [13, 16], [14, 13], [14, 15]]}
# gained: {"lines": [10, 11, 12, 13, 14, 15, 16], "branches": [[11, 12], [11, 13], [13, 14], [13, 16], [14, 13], [14, 15]]}

import pytest
from script_82 import prime_length


def test_prime_length_empty_string():
    """Test that empty string returns False (length 0)"""
    assert prime_length('') == False


def test_prime_length_single_character():
    """Test that single character string returns False (length 1)"""
    assert prime_length('a') == False


def test_prime_length_composite_number():
    """Test that string with composite length returns False"""
    assert prime_length('abcd') == False  # length 4, composite


def test_prime_length_prime_number():
    """Test that string with prime length returns True"""
    assert prime_length('ab') == True  # length 2, prime
    assert prime_length('abc') == True  # length 3, prime
    assert prime_length('Hello') == True  # length 5, prime
    assert prime_length('abcdcba') == True  # length 7, prime
    assert prime_length('kittens') == True  # length 7, prime


def test_prime_length_non_prime():
    """Test that string with non-prime length returns False"""
    assert prime_length('orange') == False  # length 6, not prime
    assert prime_length('abcdefgh') == False  # length 8, not prime
    assert prime_length('abcdefghi') == False  # length 9, not prime
