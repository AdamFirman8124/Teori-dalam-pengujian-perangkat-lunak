# file: project/f051/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import f051


def test_remove_vowels_removes_all_vowel_cases():
    result = f051.remove_vowels("AbEcIdOfUg")
    assert result == "bcdfg"


def test_remove_vowels_keeps_consonants_and_non_letters():
    result = f051.remove_vowels("xyz 123! Y")
    assert result == "xyz 123! Y"


def test_remove_vowels_empty_string():
    assert f051.remove_vowels("") == ""
