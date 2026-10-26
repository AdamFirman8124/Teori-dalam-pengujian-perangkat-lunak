# file: project/f089/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest

from f089 import encrypt


def test_encrypt_shifts_lowercase_letters():
    # 'a' -> 'e', 'b' -> 'f' (shift of 2*2 = 4)
    assert encrypt("ab") == "ef"


def test_encrypt_wraps_around_alphabet():
    # 'w' + 4 -> wraps to 'a', 'z' + 4 -> 'd'
    assert encrypt("wxyz") == "abcd"


def test_encrypt_leaves_non_letters_unchanged():
    # Digits, punctuation, uppercase, and spaces hit the else branch
    assert encrypt("a1B c!") == "e1B g!"


def test_encrypt_empty_string():
    # Loop body never executes; still returns empty string
    assert encrypt("") == ""


def test_encrypt_full_alphabet():
    plain = "abcdefghijklmnopqrstuvwxyz"
    expected = "efghijklmnopqrstuvwxyzabcd"
    assert encrypt(plain) == expected
