# file: project/f089/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

from f089 import encrypt


def test_encrypt_lowercase_letters():
    """Covers lines 3-7: alphabet setup, loop, and the 'c in d' branch."""
    assert encrypt('abc') == 'efg'
    assert encrypt('hello') == 'lipps'


def test_encrypt_non_alphabet_chars():
    """Covers line 9: the else branch for characters not in the alphabet."""
    assert encrypt('a1! Z') == 'e1! Z'


def test_encrypt_empty_string():
    """Covers lines 3-5 and 10 with an empty input (loop body never runs)."""
    assert encrypt('') == ''


def test_encrypt_wraparound():
    """Covers the modulo wraparound at the end of the alphabet (line 7)."""
    assert encrypt('wxyz') == 'abcd'
    assert encrypt('z') == 'd'


def test_encrypt_mixed_input():
    """Covers both branches in a single call."""
    assert encrypt('Attack at dawn!') == 'Axxego ex hear!'
