# file: script_143.py:1-31
# asked: {"lines": [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], "branches": [[22, 23], [22, 31], [24, 25], [24, 26], [26, 27], [26, 29], [27, 26], [27, 28], [29, 22], [29, 30]]}
# gained: {"lines": [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], "branches": [[22, 23], [22, 31], [24, 25], [24, 26], [26, 27], [26, 29], [27, 26], [27, 28], [29, 22], [29, 30]]}

import pytest
from script_143 import words_in_sentence


def test_empty_string():
    """Test with empty string."""
    assert words_in_sentence("") == ""


def test_single_word_length_one():
    """Test with a single character word (length 1, not prime)."""
    assert words_in_sentence("a") == ""


def test_single_word_length_two():
    """Test with a word of length 2 (prime)."""
    assert words_in_sentence("ab") == "ab"


def test_single_word_length_three():
    """Test with a word of length 3 (prime)."""
    assert words_in_sentence("abc") == "abc"


def test_single_word_length_four():
    """Test with a word of length 4 (not prime, 4%2==0)."""
    assert words_in_sentence("abcd") == ""


def test_single_word_length_five():
    """Test with a word of length 5 (prime)."""
    assert words_in_sentence("abcde") == "abcde"


def test_single_word_length_six():
    """Test with a word of length 6 (not prime, 6%2==0)."""
    assert words_in_sentence("abcdef") == ""


def test_single_word_length_seven():
    """Test with a word of length 7 (prime)."""
    assert words_in_sentence("abcdefg") == "abcdefg"


def test_multiple_words_mixed_lengths():
    """Test with multiple words of various lengths."""
    assert words_in_sentence("This is a test") == "is"


def test_multiple_words_all_prime():
    """Test with multiple words all having prime lengths."""
    assert words_in_sentence("ab go for") == "ab go for"


def test_multiple_words_no_prime():
    """Test with multiple words having no prime lengths."""
    assert words_in_sentence("a word") == ""


def test_word_length_nine():
    """Test with word of length 9 (not prime, 9%3==0)."""
    assert words_in_sentence("abcdefghi") == ""


def test_word_length_eleven():
    """Test with word of length 11 (prime)."""
    assert words_in_sentence("abcdefghijk") == "abcdefghijk"


def test_mixed_prime_and_non_prime():
    """Test with a mix of prime and non-prime length words."""
    assert words_in_sentence("I am going to the store") == "am going to the store"


def test_example_one():
    """Test example 1 from docstring."""
    assert words_in_sentence("This is a test") == "is"


def test_example_two():
    """Test example 2 from docstring."""
    assert words_in_sentence("lets go for swimming") == "go for"
