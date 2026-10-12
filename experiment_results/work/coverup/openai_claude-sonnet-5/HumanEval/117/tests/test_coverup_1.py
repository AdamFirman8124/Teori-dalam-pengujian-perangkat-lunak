# file: script_117.py:1-22
# asked: {"lines": [14, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[15, 16], [15, 22], [17, 18], [17, 20], [18, 17], [18, 19], [20, 15], [20, 21]]}
# gained: {"lines": [14, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[15, 16], [15, 22], [17, 18], [17, 20], [18, 17], [18, 19], [20, 15], [20, 21]]}

import pytest
from script_117 import select_words


def test_select_words_basic_case():
    """Test basic case with words containing specific number of consonants"""
    result = select_words("Mary had a little lamb", 4)
    assert result == ["little"]


def test_select_words_multiple_matches():
    """Test case with multiple matching words"""
    result = select_words("Mary had a little lamb", 3)
    assert result == ["Mary", "lamb"]


def test_select_words_no_matches():
    """Test case with no matching words"""
    result = select_words("simple white space", 2)
    assert result == []


def test_select_words_world_example():
    """Test world example with 4 consonants"""
    result = select_words("Hello world", 4)
    assert result == ["world"]


def test_select_words_uncle_example():
    """Test Uncle sam example"""
    result = select_words("Uncle sam", 3)
    assert result == ["Uncle"]


def test_select_words_empty_string():
    """Test empty string returns empty list"""
    result = select_words("", 0)
    assert result == []


def test_select_words_single_word():
    """Test single word that matches"""
    result = select_words("test", 3)
    assert result == ["test"]


def test_select_words_single_word_no_match():
    """Test single word that doesn't match"""
    result = select_words("aei", 2)
    assert result == []


def test_select_words_all_vowels():
    """Test word with all vowels"""
    result = select_words("aeiou", 0)
    assert result == ["aeiou"]


def test_select_words_mixed_case():
    """Test that uppercase and lowercase are handled correctly"""
    result = select_words("BCD fgh JKL", 3)
    assert result == ["BCD", "fgh", "JKL"]


def test_select_words_zero_consonants():
    """Test finding words with zero consonants"""
    result = select_words("a ee i oo u", 0)
    assert result == ["a", "ee", "i", "oo", "u"]
