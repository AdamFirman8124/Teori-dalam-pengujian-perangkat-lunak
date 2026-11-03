# file: project/f118/__init__.py:1-11
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}

import pytest

from f118 import get_closest_vowel


def test_word_shorter_than_three_returns_empty_string():
    # Covers lines 3-4: early return for words shorter than 3 characters.
    assert get_closest_vowel("") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("ab") == ""


def test_vowel_between_consonants_is_returned():
    # Covers lines 6-10: the loop finds a vowel whose neighbours are consonants.
    assert get_closest_vowel("full") == "u"
    assert get_closest_vowel("yogurt") == "u"


def test_uppercase_vowel_between_consonants_is_returned():
    # The vowel set contains uppercase letters as well.
    assert get_closest_vowel("bAd") == "A"
    assert get_closest_vowel("FULL") == "U"


def test_word_without_vowels_returns_empty_string():
    # Covers the false branch of line 8 and line 11 (loop exhausts, no match).
    assert get_closest_vowel("xyz") == ""
    assert get_closest_vowel("bcdfg") == ""


def test_vowel_with_vowel_neighbour_is_skipped():
    # Covers the false branches of line 9: candidate vowel touches another vowel.
    assert get_closest_vowel("quick") == ""  # 'i' preceded by 'u'; 'u' followed by 'i'
    assert get_closest_vowel("baa") == ""    # word[i+1] is a vowel
    assert get_closest_vowel("oat") == ""    # word[i-1] is a vowel


def test_only_interior_positions_are_examined():
    # The loop range is len(word)-2 .. 1, so vowels at the edges are never candidates.
    assert get_closest_vowel("aXe") == ""
    assert get_closest_vowel("XaX") == "a"
