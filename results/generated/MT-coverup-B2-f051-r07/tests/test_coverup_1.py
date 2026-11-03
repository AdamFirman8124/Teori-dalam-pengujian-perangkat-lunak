# file: project/f051/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f051 import remove_vowels


def test_remove_vowels_removes_all_vowels():
    """Line 3: the join/comprehension must execute and strip vowels."""
    assert remove_vowels("hello") == "hll"


def test_remove_vowels_mixed_case():
    """Both upper- and lower-case vowels are removed (s.lower() branch)."""
    assert remove_vowels("AbEcIdOfUg") == "bcdfg"


def test_remove_vowels_no_vowels():
    """A string without vowels is returned unchanged."""
    assert remove_vowels("rhythm") == "rhythm"


def test_remove_vowels_empty_string():
    """An empty string yields an empty string."""
    assert remove_vowels("") == ""


def test_remove_vowels_only_vowels():
    """A string consisting only of vowels yields an empty string."""
    assert remove_vowels("AEIOUaeiou") == ""


def test_remove_vowels_non_alpha_characters_kept():
    """Digits, punctuation and whitespace are preserved."""
    assert remove_vowels("a1b2c3! ?") == "1b2c3! ?"
