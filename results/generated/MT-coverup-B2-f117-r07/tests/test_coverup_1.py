# file: project/f117/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}

from f117 import select_words


def test_select_words_empty_string():
    """Empty input: the outer loop never runs, result stays empty."""
    assert select_words("", 0) == []
    assert select_words("", 3) == []


def test_select_words_basic_match():
    """Words whose consonant count equals n are selected."""
    assert select_words("Mary had a little lamb", 4) == ["little"]
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]


def test_select_words_no_match():
    """No word has exactly n consonants -> empty result."""
    assert select_words("simple white space", 2) == []


def test_select_words_case_insensitive_vowels():
    """Uppercase vowels are excluded from the consonant count too."""
    assert select_words("AEIOU aeiou", 0) == ["AEIOU", "aeiou"]


def test_select_words_mixed_case():
    """Mixed-case words count consonants case-insensitively."""
    assert select_words("Hello World", 4) == ["World"]
    assert select_words("Hello World", 3) == ["Hello"]


def test_select_words_punctuation_counts_as_consonant():
    """Non-alphabetic characters are treated as consonants."""
    assert select_words("a!b", 2) == ["a!b"]
    assert select_words("a!b", 1) == []


def test_select_words_zero_consonants():
    """Words made only of vowels match n=0."""
    assert select_words("a e i o u xyz", 0) == ["a", "e", "i", "o", "u"]


def test_select_words_multiple_matches_preserve_order():
    """Matches are appended in order of appearance."""
    assert select_words("uncle andy", 3) == ["uncle", "andy"]
