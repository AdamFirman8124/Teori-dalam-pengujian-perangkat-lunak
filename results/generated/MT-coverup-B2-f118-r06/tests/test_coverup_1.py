# file: project/f118/__init__.py:1-11
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}

from f118 import get_closest_vowel


def test_get_closest_vowel_returns_empty_for_short_word():
    assert get_closest_vowel("ab") == ""


def test_get_closest_vowel_returns_rightmost_isolated_vowel():
    assert get_closest_vowel("abecid") == "i"
    assert get_closest_vowel("cAt") == "A"


def test_get_closest_vowel_returns_empty_when_no_vowel_is_isolated():
    assert get_closest_vowel("boat") == ""
    assert get_closest_vowel("xyz") == ""
