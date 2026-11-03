# file: project/f089/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest

from f089 import encrypt


def test_encrypt_shifts_lowercase_letters():
    # Each lowercase letter is shifted forward by 4 positions.
    assert encrypt('abcd') == 'efgh'
    assert encrypt('hello') == 'lipps'


def test_encrypt_wraps_around_alphabet():
    # 'w' -> 'a', 'x' -> 'b', 'y' -> 'c', 'z' -> 'd' (mod 26 wrap-around).
    assert encrypt('wxyz') == 'abcd'
    assert encrypt('z') == 'd'


def test_encrypt_leaves_non_letters_unchanged():
    # Characters not in the alphabet are appended as-is (else branch).
    assert encrypt('a1b2!') == 'e1f2!'
    assert encrypt('HELLO, World!') == 'HELLO, Wsvph!'
    assert encrypt(' ') == ' '


def test_encrypt_empty_string():
    # Loop body never executes; result is the initial empty string.
    assert encrypt('') == ''


def test_encrypt_mixed_content_roundtrip_shape():
    # Combined coverage of both branches in a single call.
    result = encrypt('attack at dawn!')
    assert result == 'exxego ex hear!'
    assert len(result) == len('attack at dawn!')
    assert all(ch == '!' for ch in result if not ch.isalpha() and ch != ' ')
