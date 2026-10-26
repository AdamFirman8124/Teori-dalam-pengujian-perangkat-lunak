# file: project/f118/__init__.py:1-11
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}

import pytest

from f118 import get_closest_vowel


def test_short_word_returns_empty():
    # Covers lines 3-4: len(word) < 3 branch (True)
    assert get_closest_vowel("") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("ca") == ""


def test_finds_closest_vowel():
    # Covers lines 6-10: vowel found with non-vowel neighbors
    assert get_closest_vowel("cat") == "a"
    assert get_closest_vowel("full") == "u"
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"


def test_no_qualifying_vowel_returns_empty():
    # Covers line 11: loop completes without a match
    assert get_closest_vowel("bcdfg") == ""
    # Vowel at last index is never checked (range stops at 1),
    # and vowel at index 0 is never checked either.
    assert get_closest_vowel("ae") == ""
    # Adjacent vowels disqualify each other.
    assert get_closest_vowel("baat") == ""
    assert get_closest_vowel("ea") == ""
    # In "quick", 'i' has vowel 'u' before it and 'u' has vowel 'i'
    # after it, so neither qualifies.
    assert get_closest_vowel("quick") == ""


def test_vowel_between_vowels_skipped():
    # 'e' at index 2 has vowel neighbors, so skipped; 'a' at index 0
    # is out of range; loop ends -> line 11.
    assert get_closest_vowel("aei") == ""


def test_longer_word_picks_rightmost_qualifying_vowel():
    # Loop iterates from right to left; 'u' in "yogurt" qualifies first.
    assert get_closest_vowel("yogurts") == "u"
