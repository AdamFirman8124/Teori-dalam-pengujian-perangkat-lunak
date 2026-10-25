# file: project/f089/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import f089


def test_encrypt_letters():
    # lowercase letters shift by 4 (2*2) with wraparound
    assert f089.encrypt('abcd') == 'efgh'
    assert f089.encrypt('wxyz') == 'abcd'  # exercises the % 26 wraparound branch
    assert f089.encrypt('') == ''


def test_encrypt_non_letters():
    # non-alphabet characters (digits, punctuation, uppercase, space) are unchanged
    assert f089.encrypt('a1B! z') == 'e1B! d'
    assert f089.encrypt('123 !?') == '123 !?'
