# file: project/f051/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f051 import remove_vowels


def test_remove_vowels_empty_string():
    assert remove_vowels("") == ""


def test_remove_vowels_all_lowercase_vowels():
    assert remove_vowels("aeiou") == ""


def test_remove_vowels_all_uppercase_vowels():
    assert remove_vowels("AEIOU") == ""


def test_remove_vowels_mixed_case():
    assert remove_vowels("Hello World") == "Hll Wrld"


def test_remove_vowels_no_vowels():
    assert remove_vowels("rhythm") == "rhythm"


def test_remove_vowels_digits_and_symbols():
    assert remove_vowels("a1b2!c3") == "1b2!c3"


def test_remove_vowels_returns_str_and_does_not_mutate_input():
    text = "Programming"
    result = remove_vowels(text)
    assert isinstance(result, str)
    assert result == "Prgrmmng"
    assert text == "Programming"
