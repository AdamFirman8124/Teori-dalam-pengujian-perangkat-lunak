# file: project/f143/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}

from f143 import words_in_sentence


def test_empty_sentence():
    assert words_in_sentence("") == ""


def test_single_char_word_filtered():
    # len == 1 -> flg = 1, inner loop empty, outer condition False
    assert words_in_sentence("a") == ""
    assert words_in_sentence("a b c") == ""


def test_two_letter_word_kept():
    # len == 2 -> inner loop range(2, 2) empty, flg stays 0, kept
    assert words_in_sentence("ab") == "ab"
    assert words_in_sentence("ab cd") == "ab cd"


def test_prime_length_word_kept():
    # len == 3 prime -> inner loop runs once, len % i != 0, flg stays 0
    assert words_in_sentence("abc") == "abc"
    # len == 5 prime -> inner loop runs, never divisible
    assert words_in_sentence("abcde") == "abcde"
    # len == 7 prime
    assert words_in_sentence("abcdefg") == "abcdefg"


def test_composite_even_length_filtered():
    # len == 4 composite -> 4 % 2 == 0 sets flg = 1, filtered
    assert words_in_sentence("abcd") == ""
    # len == 6 composite -> 6 % 2 == 0 sets flg = 1, filtered
    assert words_in_sentence("abcdef") == ""
    # len == 8 composite
    assert words_in_sentence("abcdefgh") == ""


def test_composite_odd_length_filtered():
    # len == 9 composite -> 9 % 2 != 0 (False branch) then 9 % 3 == 0 (True branch)
    assert words_in_sentence("abcdefghi") == ""


def test_mixed_sentence_prime_filtering():
    # 1 filtered, 2 kept, 3 kept, 4 filtered, 5 kept
    assert words_in_sentence("a ab abc abcd abcde") == "ab abc abcde"
    # multiple spaces handling via split/join
    assert words_in_sentence("hello world") == "hello world"
    assert words_in_sentence("a abc abcd") == "abc"
