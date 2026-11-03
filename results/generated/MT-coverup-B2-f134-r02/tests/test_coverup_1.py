# file: project/f134/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f134 import check_if_last_char_is_a_letter


def test_true_when_last_word_is_single_lowercase_letter():
    # Covers line 3 (split) and line 4 with len==1 True and range check True.
    assert check_if_last_char_is_a_letter("hello a") is True


def test_true_when_last_word_is_single_uppercase_letter():
    # Uppercase letter is lowered before the ord check ('Z' -> 'z', ord 122).
    assert check_if_last_char_is_a_letter("hello Z") is True


def test_false_when_last_word_is_longer_than_one_char():
    # Covers line 4 with len(check) == 1 False (short-circuits the 'and').
    assert check_if_last_char_is_a_letter("hello world") is False


def test_false_on_empty_string():
    # ''.split(' ') -> [''], so check == '' and len(check) == 0 -> False.
    assert check_if_last_char_is_a_letter("") is False


def test_false_when_single_char_is_digit():
    # len==1 True but ord('0') == 48, below 97 -> range check False.
    assert check_if_last_char_is_a_letter("hello 0") is False


def test_false_when_single_char_is_punctuation_below_range():
    # len==1 True but ord('@') == 64, below 97 -> False.
    assert check_if_last_char_is_a_letter("hello @") is False


def test_false_when_single_char_is_punctuation_above_range():
    # len==1 True but ord('{') == 123, above 122 -> False.
    assert check_if_last_char_is_a_letter("hello {") is False


def test_false_when_last_word_is_single_non_letter_after_lowering():
    # Non-ASCII char whose .lower() is still outside a-z.
    assert check_if_last_char_is_a_letter("hello É") is False
