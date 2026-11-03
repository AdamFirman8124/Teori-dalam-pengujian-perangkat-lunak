# file: project/f089/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest

from f089 import encrypt


def test_encrypt_shifts_lowercase_letters():
    # Covers lines 3-7: builds the alphabet, iterates over s, and takes the
    # 'c in d' (True) branch, shifting each letter forward by 2*2 == 4.
    assert encrypt('abcd') == 'efgh'
    assert encrypt('hello') == 'lipps'


def test_encrypt_wraps_around_alphabet():
    # Covers the modulo wrap-around on line 7: (index + 4) % 26.
    # 'wxyz' maps back to 'abcd' (e.g. 'z' at index 25 -> 29 % 26 == 3 -> 'd').
    assert encrypt('wxyz') == 'abcd'
    assert encrypt('z') == 'd'


def test_encrypt_passes_through_non_alphabet_characters():
    # Covers lines 8-9: the else branch, where characters not present in the
    # lowercase alphabet (uppercase, digits, punctuation, spaces) are appended
    # unchanged.
    assert encrypt('a1! Z-') == 'e1! Z-'


def test_encrypt_empty_string():
    # Covers lines 3-4 and 10 with a zero-iteration loop (loop body not run).
    assert encrypt('') == ''
