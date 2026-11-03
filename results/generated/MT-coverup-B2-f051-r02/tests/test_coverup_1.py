# file: project/f051/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f051.remove_vowels."""

from f051 import remove_vowels


def test_remove_vowels_removes_lowercase_vowels():
    """Exercises the branch where characters ARE vowels (filtered out)."""
    result = remove_vowels("banana")
    assert result == "bnn"
    # Postcondition: no vowels remain
    assert all(ch.lower() not in "aeiou" for ch in result)


def test_remove_vowels_removes_uppercase_vowels():
    """Exercises the .lower() conversion branch for uppercase vowels."""
    result = remove_vowels("AEIOUaeiou")
    assert result == ""
    # Postcondition: every vowel (upper or lower case) was removed
    assert all(ch.lower() not in ["a", "e", "i", "o", "u"] for ch in result)


def test_remove_vowels_keeps_consonants_and_others():
    """Exercises the branch where characters are NOT vowels (kept)."""
    result = remove_vowels("Hello, World! 123")
    assert result == "Hll, Wrld! 123"
    # Postcondition: non-vowel characters preserved in order
    assert result == "".join(
        s for s in "Hello, World! 123" if s.lower() not in ["a", "e", "i", "o", "u"]
    )


def test_remove_vowels_no_vowels_unchanged():
    """Input without vowels passes through untouched."""
    text = "rhythm xyz"
    assert remove_vowels(text) == text


def test_remove_vowels_empty_string():
    """Empty input yields empty output."""
    assert remove_vowels("") == ""
