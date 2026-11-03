# file: project/f089/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

"""Tests for f089.encrypt covering all lines and branches (lines 3-10)."""

from f089 import encrypt


def test_encrypt_shifts_lowercase_letters():
    """Line 7: lowercase letters are shifted forward by 2*2 == 4 places."""
    assert encrypt('abcd') == 'efgh'
    assert encrypt('mnop') == 'qrst'


def test_encrypt_wraps_around_alphabet():
    """Line 7 modulo arithmetic: letters near 'z' wrap back to the start."""
    assert encrypt('wxyz') == 'abcd'
    assert encrypt('z') == 'd'


def test_encrypt_passthrough_non_alphabet_chars():
    """Lines 8-9 (else branch): characters outside the lowercase alphabet
    are appended unchanged."""
    assert encrypt('a1! Z-') == 'e1! Z-'
    assert encrypt('ABC') == 'ABC'


def test_encrypt_empty_string():
    """Lines 3-5, 10 with an empty loop body: '' maps to ''."""
    assert encrypt('') == ''


def test_encrypt_mixed_content_exercises_both_branches():
    """Both the if and else branches run within a single call.
    Uppercase letters (e.g. 'H', 'W') are not in the alphabet and are
    left unchanged by the else branch."""
    assert encrypt('Hello, World!') == 'Hipps, Wsvph!'
