# file: project/f089/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import f089


def test_encrypt_basic_lowercase(monkeypatch):
    """Lowercase letters are shifted by 4 (2*2) within the alphabet."""
    assert f089.encrypt('abcd') == 'efgh'
    assert f089.encrypt('hello') == 'lipps'


def test_encrypt_wraparound():
    """Letters near the end of the alphabet wrap around to the start."""
    assert f089.encrypt('wxyz') == 'abcd'
    assert f089.encrypt('z') == 'd'
    assert f089.encrypt('v') == 'z'


def test_encrypt_non_lowercase_passthrough():
    """Characters not in the lowercase alphabet are appended unchanged."""
    assert f089.encrypt('ABC') == 'ABC'
    assert f089.encrypt('Hello, World! 123') == 'Hipps, Wsvph! 123'
    assert f089.encrypt('') == ''
    assert f089.encrypt('a-b_c?') == 'e-f_g?'
