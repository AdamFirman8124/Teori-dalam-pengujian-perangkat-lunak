# file: project/f117/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}

import pytest

from f117 import select_words


def test_select_words_basic_match():
    """Words with exactly n consonants are selected."""
    assert select_words("Mary had a little lamb", 4) == ["little"]
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]


def test_select_words_no_match_returns_empty():
    """No word has exactly n consonants -> empty list."""
    assert select_words("simple little sentence here", 10) == []


def test_select_words_empty_string():
    """Empty input string -> empty list (loop body never runs)."""
    assert select_words("", 2) == []


def test_select_words_zero_consonants():
    """Words made only of vowels match n=0 (uppercase vowels lowered)."""
    assert select_words("aE I oU xyz", 0) == ["aE", "I", "oU"]


def test_select_words_mixed_case_consonants():
    """Uppercase consonants count too (branch on .lower())."""
    # "BCD" -> B, C, D are consonants (3); "def" -> d, f (2)
    assert select_words("BCD def", 3) == ["BCD"]
    assert select_words("BCD def", 2) == ["def"]
    # "ABC" has only 2 consonants: A is a vowel
    assert select_words("ABC def", 2) == ["ABC", "def"]


def test_select_words_multiple_matches_preserve_order():
    """Multiple matching words are returned in original order."""
    # "bird" -> b, r, d (3); "fish" -> f, s, h (3)
    # "cat" -> c, t (2); "dog" -> d, g (2)
    result = select_words("cat dog bird fish", 3)
    assert result == ["bird", "fish"]
    result2 = select_words("cat dog bird fish", 2)
    assert result2 == ["cat", "dog"]


def test_select_words_no_state_pollution():
    """Repeated calls are independent (no shared mutable state)."""
    first = select_words("hello", 3)
    second = select_words("hello", 3)
    assert first == ["hello"]
    assert second == ["hello"]
    assert first is not second
