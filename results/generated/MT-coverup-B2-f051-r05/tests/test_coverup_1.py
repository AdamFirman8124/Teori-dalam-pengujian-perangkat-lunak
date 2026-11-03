# file: project/f051/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f051 import remove_vowels


def test_remove_vowels_removes_lowercase_vowels():
    """Vowels (condition False branch) are removed, consonants kept."""
    assert remove_vowels("banana") == "bnn"


def test_remove_vowels_removes_uppercase_vowels():
    """Uppercase vowels exercise the s.lower() path and are removed."""
    assert remove_vowels("Apple ORANGE") == "ppl RNG"


def test_remove_vowels_keeps_non_vowel_characters():
    """Non-letters, digits and spaces hit the condition True branch."""
    assert remove_vowels("xyz 123!@#") == "xyz 123!@#"


def test_remove_vowels_empty_string():
    """Empty input yields empty output (comprehension body never runs)."""
    assert remove_vowels("") == ""


def test_remove_vowels_all_vowels_mixed_case():
    """A string of only vowels (both cases) yields an empty result."""
    assert remove_vowels("AEIOUaeiou") == ""


def test_remove_vowels_returns_str_type():
    """The result is always a plain str built by ''.join."""
    result = remove_vowels("Testing 42")
    assert isinstance(result, str)
    assert result == "Tstng 42"
