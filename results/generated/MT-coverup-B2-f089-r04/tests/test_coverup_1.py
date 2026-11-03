# file: project/f089/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest

from f089 import encrypt


def test_encrypt_empty_string():
    # Covers line 10 (return) without entering the loop body.
    assert encrypt('') == ''


def test_encrypt_lowercase_letters():
    # Covers lines 3-7 (the `c in d` true branch), including wrap-around.
    # Shift is 2*2 = 4 positions forward in the alphabet.
    assert encrypt('a') == 'e'
    assert encrypt('v') == 'z'
    # 'z' wraps around: index 25 + 4 = 29 % 26 = 3 -> 'd'
    assert encrypt('z') == 'd'
    assert encrypt('wxyz') == 'abcd'
    assert encrypt('hello') == 'lipps'


def test_encrypt_non_lowercase_characters():
    # Covers lines 8-9 (the else branch): uppercase, digits, punctuation,
    # and whitespace are passed through unchanged.
    assert encrypt('ABC') == 'ABC'
    assert encrypt('0123') == '0123'
    assert encrypt('!@#') == '!@#'
    assert encrypt(' ') == ' '


def test_encrypt_mixed_characters():
    # Exercises both branches of the if/else in a single call.
    # Only lowercase letters are shifted; uppercase letters, punctuation,
    # and digits are left untouched.
    assert encrypt('Hello, World!') == 'Hipps, Wsvph!'
    assert encrypt('abc XYZ 123') == 'efg XYZ 123'


def test_encrypt_is_bijective_with_shift_four():
    # Postcondition: applying the inverse shift recovers the original text.
    d = 'abcdefghijklmnopqrstuvwxyz'
    original = 'attack at dawn, 04:00!'
    shifted = encrypt(original)
    assert shifted == 'exxego ex hear, 04:00!'
    recovered = ''.join(
        d[(d.index(c) - 4) % 26] if c in d else c
        for c in shifted
    )
    assert recovered == original
