# file: project/f048/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

import pytest

from f048 import is_palindrome


def test_is_palindrome_true_even_length():
    # Exercises lines 3-4 (loop, comparisons) and line 6 (return True)
    assert is_palindrome("abba") is True


def test_is_palindrome_true_odd_length():
    # Exercises lines 3-4 and line 6 with an odd-length string
    assert is_palindrome("aba") is True


def test_is_palindrome_true_single_char():
    # Loop runs once, comparison passes, line 6 executes
    assert is_palindrome("a") is True


def test_is_palindrome_true_empty_string():
    # Loop body never runs (range(0)); line 6 executes directly
    assert is_palindrome("") is True


def test_is_palindrome_false_early_mismatch():
    # Exercises line 5 (return False) on the first iteration
    assert is_palindrome("ab") is False


def test_is_palindrome_false_late_mismatch():
    # Exercises line 5 after several successful comparisons
    assert is_palindrome("abcda") is False


def test_is_palindrome_false_single_char_mismatch():
    # Loop runs once, comparison fails, line 5 executes
    assert is_palindrome("ab") is False
