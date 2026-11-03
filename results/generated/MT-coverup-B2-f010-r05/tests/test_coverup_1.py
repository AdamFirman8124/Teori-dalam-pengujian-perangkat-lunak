# file: project/f010/__init__.py:6-16
# asked: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}
# gained: {"lines": [8, 9, 11, 13, 14, 16], "branches": [[8, 9], [8, 11], [13, 14], [13, 16]]}

import f010
from f010 import make_palindrome


def test_empty_string_returns_empty(monkeypatch):
    """Lines 8-9: empty input short-circuits to '' without calling is_palindrome."""
    calls = []

    def spy(s):
        calls.append(s)
        return True

    monkeypatch.setattr(f010, 'is_palindrome', spy)
    assert make_palindrome('') == ''
    assert calls == []  # early return must bypass the while loop entirely


def test_already_palindrome_skips_loop():
    """Lines 11, 13, 16: loop condition false on first check; string returned unchanged."""
    assert make_palindrome('aba') == 'aba'
    assert make_palindrome('x') == 'x'
    assert make_palindrome('racecar') == 'racecar'


def test_loop_executes_until_palindromic_suffix():
    """Lines 13-14: loop body runs; result is string + reversed non-palindromic prefix."""
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'
    assert make_palindrome('abc') == 'abcba'


def test_loop_iteration_count(monkeypatch):
    """Verifies the while loop checks successive suffixes until a palindrome is found."""
    original = f010.is_palindrome
    calls = []

    def spy(s):
        calls.append(s)
        return original(s)

    monkeypatch.setattr(f010, 'is_palindrome', spy)
    assert make_palindrome('abcd') == 'abcdcba'
    # suffixes probed: 'abcd' (no), 'bcd' (no), 'cd' (no), 'd' (yes) -> 4 iterations
    assert calls == ['abcd', 'bcd', 'cd', 'd']
