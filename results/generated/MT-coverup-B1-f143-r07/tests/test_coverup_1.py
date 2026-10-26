# file: project/f143/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}

import pytest

from f143 import words_in_sentence


def test_empty_sentence_returns_empty_string():
    result = words_in_sentence("")
    assert result == ""
    assert isinstance(result, str)


def test_single_character_word_is_dropped():
    # len == 1 -> flg = 1 -> excluded
    assert words_in_sentence("a") == ""
    assert words_in_sentence("I a b") == ""


def test_two_letter_word_is_kept():
    # loop body never runs, but len == 2 forces inclusion
    assert words_in_sentence("ab") == "ab"
    assert words_in_sentence("go to it") == "go to it"


def test_prime_length_word_is_kept():
    # len 3 and 5: loop runs, no divisor found -> flg stays 0
    assert words_in_sentence("abc") == "abc"
    assert words_in_sentence("abcde") == "abcde"


def test_composite_length_word_is_dropped():
    # len 4 and 6: loop finds a divisor -> flg = 1
    assert words_in_sentence("abcd") == ""
    assert words_in_sentence("abcdef") == ""


def test_mixed_sentence_filters_only_prime_length_words():
    sentence = "a ab abc abcd abcde abcdef abcdefg"
    assert words_in_sentence(sentence) == "ab abc abcde abcdefg"


def test_whitespace_only_sentence_returns_empty_string():
    assert words_in_sentence("   ") == ""
    assert words_in_sentence("\t\n ") == ""


def test_original_sentence_is_not_mutated():
    sentence = "a ab abc abcd"
    snapshot = sentence
    words_in_sentence(sentence)
    assert sentence == snapshot
