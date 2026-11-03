# file: project/f010/__init__.py:6-16
# asked: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}
# gained: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}

import f010
from f010 import make_palindrome


def test_make_palindrome_empty_string():
    """Covers lines 8-9: the early-return branch for a falsy string."""
    assert make_palindrome('') == ''


def test_make_palindrome_already_palindrome():
    """Covers lines 11, 13 and 16: non-empty input that is already a
    palindrome, so the while body (line 14) is never entered."""
    assert make_palindrome('a') == 'a'
    assert make_palindrome('racecar') == 'racecar'


def test_make_palindrome_appends_reverse_of_prefix():
    """Covers line 14: the while body executes (once here) because the
    input is not a palindrome; the shortest prefix to reverse is 'ca'."""
    assert make_palindrome('cat') == 'catac'


def test_make_palindrome_loop_runs_multiple_times():
    """Covers line 14 repeatedly: the while loop must advance
    beginning_of_suffix several times before a palindromic suffix is found.
    For 'abcd' the loop runs 3 times ('abcd', 'bcd', 'cd' are not palindromes,
    'd' is), producing 'abcd' + 'cba'. For 'abab' the loop runs once because
    the suffix 'bab' is already a palindrome, producing 'abab' + 'a'."""
    assert make_palindrome('abcd') == 'abcdcba'
    assert make_palindrome('abab') == 'ababa'


def test_make_palindrome_queries_is_palindrome_with_shrinking_suffixes(monkeypatch):
    """Verifies make_palindrome delegates to is_palindrome with successively
    shorter suffixes; monkeypatch guarantees the patch is undone afterwards."""
    calls = []
    real_is_palindrome = f010.is_palindrome

    def recording_is_palindrome(string: str) -> bool:
        calls.append(string)
        return real_is_palindrome(string)

    monkeypatch.setattr(f010, 'is_palindrome', recording_is_palindrome)

    assert make_palindrome('cat') == 'catac'
    assert calls == ['cat', 'at', 't']
