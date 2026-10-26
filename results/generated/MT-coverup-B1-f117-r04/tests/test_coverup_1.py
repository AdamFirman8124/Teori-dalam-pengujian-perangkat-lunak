# file: project/f117/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}

from f117 import select_words


def test_empty_string_no_words():
    assert select_words("", 0) == []
    assert select_words("", 3) == []
    assert select_words("   ", 0) == []


def test_single_vowel_word_zero_consonants():
    assert select_words("a", 0) == ["a"]
    assert select_words("a", 1) == []
    assert select_words("aei", 0) == ["aei"]
    assert select_words("AEIOU", 0) == ["AEIOU"]


def test_single_consonant_word():
    assert select_words("b", 1) == ["b"]
    assert select_words("B", 1) == ["B"]
    assert select_words("bcd", 3) == ["bcd"]
    assert select_words("bcDF", 4) == ["bcDF"]
    assert select_words("b", 0) == []


def test_mixed_words_true_and_false_outer_if():
    # Mary=3, had=2, a=0, little=4, lamb=3
    assert select_words("Mary had a little lamb", 4) == ["little"]
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert select_words("hello world", 4) == ["world"]
    assert select_words("hello world", 3) == ["hello"]


def test_uppercase_handling_and_multiple_matches():
    assert select_words("AEIOU xyz", 0) == ["AEIOU"]
    assert select_words("Mary lamb hello", 3) == ["Mary", "lamb", "hello"]
    assert select_words("Hello", 3) == ["Hello"]
    assert select_words("Hello", 2) == []


def test_no_match_and_all_match():
    assert select_words("abc def", 10) == []
    assert select_words("ab ac", 1) == ["ab", "ac"]
    assert select_words("ab cd", 1) == ["ab"]
    assert select_words("ab cd", 2) == ["cd"]
