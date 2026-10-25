# file: project/f143/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [11, 4], [11, 12]]}

import pytest

from f143 import words_in_sentence


def test_empty_sentence():
    assert words_in_sentence("") == ""
    assert words_in_sentence("   ") == ""


def test_single_letter_words_excluded():
    assert words_in_sentence("a") == ""
    assert words_in_sentence("a I x") == ""


def test_two_letter_words_included():
    assert words_in_sentence("hi") == "hi"
    assert words_in_sentence("hi is ok") == "hi is ok"


def test_prime_length_words_included():
    assert words_in_sentence("cat hello") == "cat hello"
    assert words_in_sentence("bb ccc eeeee ggggggg") == "bb ccc eeeee ggggggg"


def test_composite_length_words_excluded():
    assert words_in_sentence("dogs") == ""
    assert words_in_sentence("aaaa aaaaaa aaaaaaaa") == ""
    # Length 9: no divisor at i=2, divisor found at i=3
    assert words_in_sentence("aaaaaaaaa") == ""
    assert words_in_sentence("aaaaaaaaaa") == ""


def test_mixed_sentence_known_examples():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("a hi cat dogs hello world") == "hi cat hello world"


def test_all_lengths_1_to_9():
    sentence = "a bb ccc dddd eeeee ffffff ggggggg hhhhhhhh iiiiiiiii"
    assert words_in_sentence(sentence) == "bb ccc eeeee ggggggg"


def test_extra_whitespace_normalized():
    assert words_in_sentence("  hi   cat  dogs ") == "hi cat"


@pytest.mark.parametrize(
    "sentence,expected",
    [
        ("", ""),
        ("a", ""),
        ("ab", "ab"),
        ("abc", "abc"),
        ("abcd", ""),
        ("abcde", "abcde"),
        ("abcdef", ""),
        ("abcdefg", "abcdefg"),
        ("abcdefgh", ""),
        ("abcdefghi", ""),
        ("abcdefghij", ""),
        ("abcdefghijk", "abcdefghijk"),
        # one(3) two(3) three(5) four(4) five(4) six(3) seven(5)
        ("one two three four five six seven", "one two three six seven"),
    ],
)
def test_words_in_sentence_parametrized(sentence, expected):
    result = words_in_sentence(sentence)
    assert result == expected
    assert isinstance(result, str)
