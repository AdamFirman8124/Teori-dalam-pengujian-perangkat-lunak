# file: script_118.py:1-24
# asked: {"lines": [16, 17, 19, 20, 21, 22, 23, 24], "branches": [[16, 17], [16, 19], [20, 21], [20, 24], [21, 20], [21, 22], [22, 20], [22, 23]]}
# gained: {"lines": [16, 17, 19, 20, 21, 22, 23, 24], "branches": [[16, 17], [16, 19], [20, 21], [20, 24], [21, 20], [21, 22], [22, 20], [22, 23]]}

import pytest
from script_118 import get_closest_vowel


def test_get_closest_vowel_word_length_less_than_3():
    """Test that words with length < 3 return empty string."""
    assert get_closest_vowel("") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("ab") == ""


def test_get_closest_vowel_found():
    """Test that closest vowel between consonants is found."""
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("bac") == "a"
    assert get_closest_vowel("BAC") == "A"
    assert get_closest_vowel("bec") == "e"
    assert get_closest_vowel("BEC") == "E"
    assert get_closest_vowel("bic") == "i"
    assert get_closest_vowel("BIC") == "I"
    assert get_closest_vowel("boc") == "o"
    assert get_closest_vowel("BOC") == "O"


def test_get_closest_vowel_no_vowel_between_consonants():
    """Test that words without vowels between consonants return empty string."""
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("bcdfg") == ""
    assert get_closest_vowel("xyz") == ""


def test_get_closest_vowel_vowel_not_between_consonants():
    """Test vowels at boundaries or adjacent to other vowels don't count."""
    assert get_closest_vowel("aei") == ""
    assert get_closest_vowel("abc") == ""
    assert get_closest_vowel("bae") == ""
    assert get_closest_vowel("eab") == ""


def test_get_closest_vowel_multiple_vowels_returns_rightmost():
    """Test that the rightmost vowel between consonants is returned."""
    assert get_closest_vowel("bacar") == "a"
    assert get_closest_vowel("bicep") == "e"
