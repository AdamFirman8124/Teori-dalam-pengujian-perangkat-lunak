# file: project/f117/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}

from f117 import select_words


def test_select_words_empty_string():
    """Empty input: the loops never execute and an empty list is returned."""
    assert select_words("", 3) == []


def test_select_words_selects_matching_words():
    """Only words whose consonant count equals n are selected."""
    assert select_words("hello world", 4) == ["world"]


def test_select_words_no_match_returns_empty():
    """When no word has exactly n consonants, an empty list is returned."""
    assert select_words("hello world", 5) == []


def test_select_words_multiple_matches_preserve_order():
    """Several matching words are all returned in their original order."""
    assert select_words("simple little test", 4) == ["simple", "little"]


def test_select_words_is_case_insensitive():
    """Uppercase consonants are counted via the .lower() branch."""
    assert select_words("HELLO World", 4) == ["World"]


def test_select_words_zero_consonants():
    """A word made only of vowels matches n == 0; 'y' counts as a consonant."""
    assert select_words("aeiou aeiouy", 0) == ["aeiou"]


def test_select_words_non_letter_characters_count():
    """Non-vowel characters such as digits count as consonants."""
    assert select_words("a1b xy", 2) == ["a1b", "xy"]
