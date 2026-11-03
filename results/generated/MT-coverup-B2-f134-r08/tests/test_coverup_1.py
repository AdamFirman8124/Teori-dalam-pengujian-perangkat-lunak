# file: project/f134/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f134 import check_if_last_char_is_a_letter


def test_true_single_lowercase_letter():
    # Last word is a single lowercase letter -> True branch of line 4
    assert check_if_last_char_is_a_letter("hello world a") is True


def test_true_single_uppercase_letter():
    # Uppercase letter is lowered before the ord check -> still True
    assert check_if_last_char_is_a_letter("hello Z") is True


def test_false_multi_char_last_word():
    # Last word has more than one character -> False (short-circuits before ord)
    assert check_if_last_char_is_a_letter("apple pie") is False


def test_false_single_digit():
    # Single character but not a letter (ord('7') == 55) -> False
    assert check_if_last_char_is_a_letter("abc 7") is False


def test_false_single_punctuation():
    # Single character but not a letter (ord('!') == 33) -> False
    assert check_if_last_char_is_a_letter("hi !") is False


def test_false_empty_string():
    # "".split(' ') == [''] -> check is '' -> len != 1 -> False (no ord crash)
    assert check_if_last_char_is_a_letter("") is False


def test_false_trailing_space():
    # "word ".split(' ') == ['word', ''] -> check is '' -> False
    assert check_if_last_char_is_a_letter("word ") is False
