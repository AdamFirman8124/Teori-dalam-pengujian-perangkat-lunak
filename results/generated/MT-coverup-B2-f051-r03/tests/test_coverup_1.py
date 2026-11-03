# file: project/f051/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f051 import remove_vowels


def test_remove_vowels_removes_lowercase_vowels():
    assert remove_vowels("banana") == "bnn"


def test_remove_vowels_removes_uppercase_vowels():
    assert remove_vowels("ApPlE") == "pPl"


def test_remove_vowels_keeps_non_vowel_characters():
    assert remove_vowels("rhythm! 123") == "rhythm! 123"


def test_remove_vowels_empty_string():
    assert remove_vowels("") == ""


def test_remove_vowels_only_vowels():
    assert remove_vowels("aeiouAEIOU") == ""


def test_remove_vowels_mixed_case_and_symbols():
    result = remove_vowels("Héllo, WOrld!")
    assert result == "Héll, Wrld!"
    assert "a" not in result.lower()
    assert "e" not in result.lower()
    assert "i" not in result.lower()
    assert "o" not in result.lower()
    assert "u" not in result.lower()
