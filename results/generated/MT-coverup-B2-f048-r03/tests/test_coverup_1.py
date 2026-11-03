# file: project/f048/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

import pytest

from f048 import is_palindrome


def test_empty_string_returns_true():
    # Empty string: loop body never executes; control falls through to `return True` (line 6).
    assert is_palindrome("") is True


def test_single_character_returns_true():
    # Loop executes once (lines 3-4), the comparison matches, so `return True` (line 6).
    assert is_palindrome("x") is True


def test_even_length_palindrome_returns_true():
    # Several loop iterations (lines 3-4) with every comparison matching -> `return True` (line 6).
    assert is_palindrome("abba") is True


def test_odd_length_palindrome_returns_true():
    assert is_palindrome("racecar") is True


def test_immediate_mismatch_returns_false():
    # First comparison fails, exercising the early `return False` (line 5).
    assert is_palindrome("ab") is False


def test_mismatch_after_matching_pair_returns_false():
    # One comparison succeeds, then a later one fails -> `return False` (line 5).
    assert is_palindrome("abca") is False


def test_result_is_real_bool():
    # Postcondition: the function returns actual bool values, not merely truthy/falsy objects.
    assert isinstance(is_palindrome("abba"), bool)
    assert isinstance(is_palindrome("abc"), bool)
