# file: script_10.py:6-26
# asked: {"lines": [18, 19, 21, 23, 24, 26], "branches": [[18, 19], [18, 21], [23, 24], [23, 26]]}
# gained: {"lines": [18, 19, 21, 23, 24, 26], "branches": [[18, 19], [18, 21], [23, 24], [23, 26]]}

import pytest

from script_10 import make_palindrome


@pytest.fixture(autouse=True)
def _isolate(monkeypatch):
    yield


def test_make_palindrome_empty_string():
    # Executes line 18-19: the early-return branch for empty input.
    result = make_palindrome('')
    assert result == ''
    assert result == result[::-1]


def test_make_palindrome_single_char():
    # 'a' is already a palindrome, so the while loop never runs (line 23/24 skipped).
    result = make_palindrome('a')
    assert result == 'a'
    assert result.startswith('a')
    assert result == result[::-1]


def test_make_palindrome_already_palindrome():
    # Loop body (line 24) never executes; length preserved.
    result = make_palindrome('racecar')
    assert result == 'racecar'
    assert result == result[::-1]


def test_make_palindrome_cat():
    # Exercises while loop: 'cat' -> 'at' -> 't' (palindrome) requires two iterations.
    result = make_palindrome('cat')
    assert result == 'catac'
    assert result.startswith('cat')
    assert result == result[::-1]


def test_make_palindrome_cata():
    # Exercises while loop: 'cata' -> 'ata' (palindrome), one iteration.
    result = make_palindrome('cata')
    assert result == 'catac'
    assert result.startswith('cata')
    assert result == result[::-1]


def test_make_palindrome_single_letter_prefix():
    # beginning_of_suffix increments then loop ends immediately: 'ab' -> 'b'.
    result = make_palindrome('ab')
    assert result == 'aba'
    assert result.startswith('ab')
    assert result == result[::-1]


def test_make_palindrome_long_run():
    # Longer loop with multiple iterations.
    result = make_palindrome('abcd')
    assert result == 'abcdcba'
    assert result.startswith('abcd')
    assert result == result[::-1]
