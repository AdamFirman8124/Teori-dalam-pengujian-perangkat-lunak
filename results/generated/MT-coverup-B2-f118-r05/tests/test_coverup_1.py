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
    assert get_closest_vowel("banana") == "a"
    assert get_closest_vowel("computer") == "e"


def test_no_qualifying_vowel_returns_empty():
    # Covers line 11: loop completes without a match
    assert get_closest_vowel("bcdfg") == ""
    # Adjacent vowels disqualify each other: in "quick", "i" is
    # preceded by "u" and "u" is followed by "i".
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("quickly") == ""
    assert get_closest_vowel("baat") == ""


def test_vowel_between_vowels_skipped():
    # "e" at index 1 has vowel neighbors, so it is skipped;
    # the loop then ends -> line 11.
    assert get_closest_vowel("aei") == ""


def test_disqualified_vowel_skipped_then_earlier_vowel_found():
    # In "catee", "e" at index 3 is followed by a vowel and is
    # skipped; "a" at index 1 qualifies and is returned.
    assert get_closest_vowel("catee") == "a"


def test_longer_word_picks_rightmost_qualifying_vowel():
    # Loop iterates from right to left; in "yogurt", "u" at
    # index 3 qualifies before "o" at index 1 is examined.
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("banana") == "a"
