# file: project/f134/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f134 import check_if_last_char_is_a_letter


def test_last_char_is_letter_true():
    # Last word is a single lowercase letter -> True
    assert check_if_last_char_is_a_letter("hello world a") is True


def test_last_char_is_letter_true_uppercase():
    # Last word is a single uppercase letter -> True (lower() branch)
    assert check_if_last_char_is_a_letter("hello world Z") is True


def test_last_word_multiple_chars_false():
    # Last word has more than one character -> False
    assert check_if_last_char_is_a_letter("hello world") is False


def test_last_char_not_letter_false():
    # Last word is a single non-letter character -> False
    assert check_if_last_char_is_a_letter("hello world 1") is False


def test_empty_string_false():
    # Empty string: check == '', len != 1 short-circuits before ord() -> False
    assert check_if_last_char_is_a_letter("") is False


def test_trailing_space_false():
    # Trailing space yields an empty last token -> False
    assert check_if_last_char_is_a_letter("hello a ") is False
