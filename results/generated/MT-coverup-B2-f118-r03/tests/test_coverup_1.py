# file: project/f118/__init__.py:1-11
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}

import pytest

from f118 import get_closest_vowel


def test_words_shorter_than_three_characters_return_empty_string():
    """Covers lines 3-4: early return when len(word) < 3."""
    assert get_closest_vowel("") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("ab") == ""


def test_isolated_vowel_is_returned():
    """Covers lines 6-10: a vowel with consonants on both sides is returned."""
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("cat") == "a"


def test_loop_continues_past_rejected_vowel():
    """Covers the loop iterating on after a vowel fails the neighbour check."""
    # 'E' at index 4 is rejected because word[5] == 'e' is a vowel;
    # the loop then continues and 'a' at index 1 is returned.
    assert get_closest_vowel("XaXbEe") == "a"


def test_vowel_followed_by_vowel_is_rejected():
    """Covers the False branch of line 9 caused by word[i+1] being a vowel."""
    assert get_closest_vowel("bae") == ""
    assert get_closest_vowel("aei") == ""


def test_vowel_preceded_by_vowel_is_rejected():
    """Covers the False branch of line 9 caused by word[i-1] being a vowel."""
    # 'i' at index 2 is rejected because word[1] == 'u' is a vowel.
    assert get_closest_vowel("quick") == ""


def test_no_eligible_vowel_returns_empty_string():
    """Covers line 11: the loop finishes without ever returning a vowel."""
    assert get_closest_vowel("bcdfg") == ""   # no vowels at all
    assert get_closest_vowel("aeiou") == ""   # vowels, but none isolated
    assert get_closest_vowel("aXy") == ""     # index 0 is never examined
    assert get_closest_vowel("bca") == ""     # last index is never examined
