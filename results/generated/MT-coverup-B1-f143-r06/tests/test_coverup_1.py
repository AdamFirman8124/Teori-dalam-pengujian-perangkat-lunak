# file: project/f143/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}

from f143 import words_in_sentence


def test_empty_sentence():
    assert words_in_sentence("") == ""


def test_single_char_word_filtered():
    # len(word) == 1 -> flg = 1, inner loop empty, final if False
    assert words_in_sentence("a") == ""
    assert words_in_sentence("a b c") == ""


def test_two_letter_word_kept():
    # len(word) == 2 -> flg stays 0, inner loop empty, flg == 0 True
    assert words_in_sentence("ab") == "ab"
    assert words_in_sentence("ab cd") == "ab cd"


def test_prime_length_words_kept():
    # range(2, len(word)) non-empty, len % i != 0 so flg stays 0, final if True
    assert words_in_sentence("abc") == "abc"
    assert words_in_sentence("abcde") == "abcde"
    assert words_in_sentence("abcdefg") == "abcdefg"


def test_composite_length_words_filtered():
    # range(2, len(word)) non-empty, len % i == 0 for some i so flg = 1, final if False
    assert words_in_sentence("abcd") == ""
    assert words_in_sentence("abcdef") == ""
    assert words_in_sentence("abcdefghi") == ""


def test_mixed_sentence():
    # covers len==1 True/False, inner loop empty/non-empty,
    # inner if True/False, outer final if True/False in one call
    assert words_in_sentence("a ab abc abcd abcde") == "ab abc abcde"
    assert words_in_sentence("I am to be or not to be") == "am to be or not to be"
