# file: script_10.py:6-26
# asked: {"lines": [18, 19, 21, 23, 24, 26], "branches": [[18, 19], [18, 21], [23, 24], [23, 26]]}
# gained: {"lines": [18, 19, 21, 23, 24, 26], "branches": [[18, 19], [18, 21], [23, 24], [23, 26]]}

from script_10 import make_palindrome
# step 1/1 done: lines 18-26 covered - '' + palindrome logic works
def test_make_palindrome_empty():
    assert make_palindrome('') == ''

def test_make_palindrome_already_palindrome():
    assert make_palindrome('a') == 'a'
    assert make_palindrome('aba') == 'aba'

def test_make_palindrome_cat_needs_two_char_completion():
    result = make_palindrome('cat')
    assert result == 'catac'
    assert result.startswith('cat')
    assert result == result[::-1]

def test_make_palindrome_cata_needs_one_char_completion():
    result = make_palindrome('cata')
    assert result == 'catac'
    assert result.startswith('cata')
    assert result == result[::-1]
# next (30s): run pytest -q --cov
