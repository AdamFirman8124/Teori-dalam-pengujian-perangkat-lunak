# file: project/f118/__init__.py:1-11
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}

from f118 import get_closest_vowel


def test_short_word_returns_empty():
    assert get_closest_vowel("") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("xy") == ""


def test_no_vowel_between_consonants_right_neighbor_vowel():
    # 'a' at index 1 has right neighbor 'a' (vowel) -> inner first condition False
    assert get_closest_vowel("aaa") == ""


def test_no_vowel_between_consonants_left_neighbor_vowel():
    # 'e' at index 1 has right neighbor 'b' (consonant) but left neighbor 'a' (vowel)
    # -> first part True, second part False
    assert get_closest_vowel("aeb") == ""


def test_finds_closest_vowel_from_right():
    # 'u' at index 3 is between 'g' and 'r' (both consonants)
    assert get_closest_vowel("yogurt") == "u"


def test_uppercase_vowel_found():
    assert get_closest_vowel("YOGURT") == "U"


def test_no_vowels_returns_empty():
    assert get_closest_vowel("bcdfg") == ""
    assert get_closest_vowel("xyz") == ""


def test_edge_vowels_ignored():
    # only index 1 is checked for len==3; index 0 and 2 are excluded
    assert get_closest_vowel("aba") == ""
    assert get_closest_vowel("ebe") == ""


def test_vowel_near_start_found():
    # loop must iterate past non-vowels to find 'u' at index 1
    assert get_closest_vowel("full") == "u"


def test_consecutive_vowels_returns_empty():
    # every vowel has at least one vowel neighbor
    assert get_closest_vowel("beauty") == ""
    assert get_closest_vowel("aei") == ""
