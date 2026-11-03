# file: project/f051/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f051 import remove_vowels


def test_remove_vowels_removes_lowercase_vowels():
    """Line 3: list comprehension filters out lowercase vowels."""
    result = remove_vowels("banana")
    assert result == "bnn"


def test_remove_vowels_removes_uppercase_vowels():
    """Line 3: s.lower() ensures uppercase vowels are also removed."""
    result = remove_vowels("AEIOUaeiou")
    assert result == ""


def test_remove_vowels_keeps_consonants_and_others():
    """Line 3: non-vowel characters (including digits, punctuation, spaces) are kept."""
    result = remove_vowels("Hello, World! 123")
    assert result == "Hll, Wrld! 123"


def test_remove_vowels_empty_string():
    """Line 3: empty input yields empty output."""
    assert remove_vowels("") == ""


def test_remove_vowels_no_vowels():
    """Line 3: string without vowels is returned unchanged."""
    assert remove_vowels("rhythm") == "rhythm"


def test_remove_vowels_mixed_case():
    """Line 3: mixed-case input has all vowels removed regardless of case,
    while consonant case is preserved."""
    assert remove_vowels("PyThOn Is FuN") == "PyThn s FN"
