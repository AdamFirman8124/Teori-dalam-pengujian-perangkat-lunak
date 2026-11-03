# file: project/f089/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

from f089 import encrypt


def test_encrypt_empty_string():
    # Covers lines 3-5 and 10 (loop body never executes).
    assert encrypt('') == ''


def test_encrypt_shifts_lowercase_letters_by_four():
    # Covers line 6 (true branch) and line 7.
    assert encrypt('abcd') == 'efgh'
    assert encrypt('attack') == 'exxego'


def test_encrypt_wraps_around_end_of_alphabet():
    # Covers line 7 including the modulo wrap-around branch.
    assert encrypt('wxyz') == 'abcd'
    assert encrypt('z') == 'd'


def test_encrypt_passes_through_non_lowercase_characters():
    # Covers line 6 (false branch) and line 9.
    assert encrypt('HELLO, WORLD! 123') == 'HELLO, WORLD! 123'
    assert encrypt('\t\n _-') == '\t\n _-'


def test_encrypt_mixed_content_exercises_both_branches():
    # Exercises both the letter-shift and pass-through branches in one call.
    assert encrypt('Hello, World! 123') == 'Hipps, Wsvph! 123'
    assert encrypt('Attack at dawn! Zz9') == 'Axxego ex hear! Zd9'
