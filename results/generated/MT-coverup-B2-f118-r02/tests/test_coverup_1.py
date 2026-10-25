# file: project/f118/__init__.py:1-11
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}

import importlib

import pytest


@pytest.fixture()
def get_closest_vowel():
    module = importlib.import_module("f118")
    return module.get_closest_vowel


def test_short_word_returns_empty(get_closest_vowel):
    assert get_closest_vowel("") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("ab") == ""


def test_vowel_between_consonants_is_returned(get_closest_vowel):
    assert get_closest_vowel("rab") == "a"
    assert get_closest_vowel("dog") == "o"


def test_uppercase_vowel_is_returned(get_closest_vowel):
    assert get_closest_vowel("rAb") == "A"
    assert get_closest_vowel("dOg") == "O"


def test_rightmost_qualifying_vowel_wins(get_closest_vowel):
    assert get_closest_vowel("rabec") == "e"


def test_vowel_with_vowel_after_is_skipped(get_closest_vowel):
    assert get_closest_vowel("baa") == ""
    assert get_closest_vowel("tree") == ""


def test_vowel_with_vowel_before_is_skipped(get_closest_vowel):
    assert get_closest_vowel("aab") == ""
    assert get_closest_vowel("eat") == ""


def test_no_vowels_returns_empty(get_closest_vowel):
    assert get_closest_vowel("bcd") == ""
    assert get_closest_vowel("xyz") == ""


def test_first_and_last_positions_are_never_considered(get_closest_vowel):
    # 'a' at index 0 and 'e' at the last index are outside the loop range.
    assert get_closest_vowel("abcde") == ""
    assert get_closest_vowel("abce") == ""
