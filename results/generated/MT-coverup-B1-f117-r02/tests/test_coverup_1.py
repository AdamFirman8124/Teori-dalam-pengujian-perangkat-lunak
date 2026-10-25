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
    # "ABC": A=vowel, B/C=consonants -> 2; "def": d/f=consonants -> 2
    assert select_words("ABC def", 2) == ["ABC", "def"]
    # "XYZ": all uppercase consonants -> 3; "ae": vowels -> 0
    assert select_words("XYZ ae", 3) == ["XYZ"]
    assert select_words("XYZ ae", 0) == ["ae"]


def test_select_words_multiple_matches_preserve_order():
    """Multiple matching words are returned in original order."""
    # cat=2, dog=2, bird=3, fish=3 consonants
    assert select_words("cat dog bird fish", 3) == ["bird", "fish"]
    assert select_words("cat dog bird fish", 2) == ["cat", "dog"]


def test_select_words_no_state_pollution():
    """Repeated calls are independent (no shared mutable state)."""
    first = select_words("hello", 3)
    second = select_words("hello", 3)
    assert first == ["hello"]
    assert second == ["hello"]
    assert first is not second
