# file: project/f051/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f051 import remove_vowels


def test_remove_vowels_removes_all_vowels_case_insensitive():
    # Executes line 3: the return statement with the list comprehension.
    result = remove_vowels("Hello World")
    assert result == "Hll Wrld"


def test_remove_vowels_keeps_non_vowel_characters():
    result = remove_vowels("rhythm & xyz 123!")
    assert result == "rhythm & xyz 123!"


def test_remove_vowels_empty_string():
    result = remove_vowels("")
    assert result == ""


def test_remove_vowels_all_vowels():
    result = remove_vowels("AEIOUaeiou")
    assert result == ""


def test_remove_vowels_returns_string_type():
    result = remove_vowels("banana")
    assert isinstance(result, str)
    assert result == "bnn"
