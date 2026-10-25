# file: project/f143/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}

from f143 import words_in_sentence


def test_empty_sentence():
    assert words_in_sentence("") == ""
    assert words_in_sentence("   ") == ""


def test_single_character_words_excluded():
    assert words_in_sentence("a") == ""
    assert words_in_sentence("a I x") == ""


def test_two_letter_words_included():
    assert words_in_sentence("hi") == "hi"
    assert words_in_sentence("hi am ok") == "hi am ok"


def test_prime_length_words_included():
    assert words_in_sentence("cat") == "cat"
    assert words_in_sentence("hello") == "hello"
    assert words_in_sentence("aa bbb ccccc ddddddd") == "aa bbb ccccc ddddddd"


def test_composite_length_words_excluded():
    assert words_in_sentence("abcd") == ""
    assert words_in_sentence("aaaa aaaaaa aaaaaaaa aaaaaaaaa") == ""


def test_mixed_sentence():
    assert words_in_sentence("a hi cat abcd hello abcdef world") == "hi cat hello world"
    assert words_in_sentence("I am a prime word test") == "am prime"
