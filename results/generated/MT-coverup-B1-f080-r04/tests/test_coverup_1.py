# file: project/f080/__init__.py:1-10
# asked: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}

import pytest

from f080 import is_happy


def test_is_happy_short_string_returns_false():
    # Covers line 3-4: len(s) < 3 branch (True path)
    assert is_happy("") is False
    assert is_happy("a") is False
    assert is_happy("ab") is False


def test_is_happy_repeated_adjacent_chars_returns_false():
    # Covers lines 6, 8-9: loop entered, adjacent-equal branch (True path)
    assert is_happy("aab") is False
    assert is_happy("abb") is False


def test_is_happy_repeated_skip_one_chars_returns_false():
    # Covers lines 6, 8-9: s[i] == s[i+2] branch (True path)
    assert is_happy("aba") is False


def test_is_happy_valid_string_returns_true():
    # Covers lines 6, 8, 10: loop completes with no early return
    assert is_happy("abc") is True
    assert is_happy("abcd") is True
    assert is_happy("abcdef") is True
