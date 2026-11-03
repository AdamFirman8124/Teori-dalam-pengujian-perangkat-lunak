# file: project/f117/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}

from f117 import select_words


def test_empty_string_returns_empty_list():
    """Covers lines 3, 4, 11 with the outer loop never executing."""
    assert select_words("", 0) == []
    assert select_words("", 4) == []


def test_words_with_matching_consonant_count_are_selected():
    """Covers lines 5-8 (consonant counting) and lines 9-10 (append on match)."""
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]


def test_no_word_matches_returns_empty_list():
    """Covers the False branch of the n_consonants == n check (line 9)."""
    assert select_words("hello world", 10) == []


def test_vowel_only_word_matches_zero_consonants():
    """Covers the False branch of the vowel check (line 7) and a zero-count match."""
    assert select_words("aeiou bcd", 0) == ["aeiou"]


def test_uppercase_vowels_are_not_counted_as_consonants():
    """Covers the .lower() normalization on line 7 for uppercase vowels."""
    assert select_words("AbE", 1) == ["AbE"]


def test_uppercase_consonants_are_counted():
    """Covers counting uppercase consonants on line 8."""
    assert select_words("BCD", 3) == ["BCD"]


def test_single_word_without_spaces():
    """Covers a single iteration of the outer loop (line 4)."""
    assert select_words("hello", 3) == ["hello"]


def test_multiple_matches_preserve_order():
    """Covers multiple appends (line 10) preserving input order."""
    assert select_words("simple white space", 3) == ["white", "space"]


def test_mixed_match_and_non_match_words():
    """Covers both branches of line 9 within a single call."""
    assert select_words("a bb ccc dddd", 2) == ["bb"]
