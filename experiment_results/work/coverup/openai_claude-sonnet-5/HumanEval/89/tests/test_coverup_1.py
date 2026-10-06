# file: script_89.py:1-19
# asked: {"lines": [12, 13, 14, 15, 16, 18, 19], "branches": [[14, 15], [14, 19], [15, 16], [15, 18]]}
# gained: {"lines": [12, 13, 14, 15, 16, 18, 19], "branches": [[14, 15], [14, 19], [15, 16], [15, 18]]}

import pytest
import sys
import os

# Add the directory containing script_89.py to the path if needed
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from script_89 import encrypt


def test_encrypt_simple():
    result = encrypt('hi')
    assert result == 'lm'


def test_encrypt_longer_string():
    result = encrypt('asdfghjkl')
    assert result == 'ewhjklnop'


def test_encrypt_two_chars():
    result = encrypt('gf')
    assert result == 'kj'


def test_encrypt_with_wrap():
    result = encrypt('et')
    assert result == 'ix'


def test_encrypt_empty_string():
    result = encrypt('')
    assert result == ''


def test_encrypt_with_non_alpha():
    result = encrypt('hello world')
    assert result == 'lipps asvph'


def test_encrypt_with_numbers():
    result = encrypt('test123')
    assert result == 'xiwx123'


def test_encrypt_with_special_chars():
    result = encrypt('a!b@c#')
    assert result == 'e!f@g#'


def test_encrypt_wrap_around():
    result = encrypt('xyz')
    assert result == 'bcd'
