# file: project/f134/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f134 import check_if_last_char_is_a_letter


def test_single_lowercase_letter_returns_true():
    # Covers the True branch: len(check) == 1 and ord in [97, 122]
    assert check_if_last_char_is_a_letter("hello world a") is True


def test_single_uppercase_letter_returns_true():
    # Covers the .lower() conversion inside the True branch
    assert check_if_last_char_is_a_letter("hello world Z") is True


def test_last_word_longer_than_one_char_returns_false():
    # Covers the False branch via len(check) != 1 (short-circuits before ord)
    assert check_if_last_char_is_a_letter("hello world") is False


def test_single_digit_returns_false():
    # Covers the False branch: len == 1 but ord('1') == 49 < 97
    assert check_if_last_char_is_a_letter("hello 1") is False


def test_single_punctuation_returns_false():
    # Covers the False branch: len == 1 but ord('!') == 33 < 97
    assert check_if_last_char_is_a_letter("hello !") is False


def test_non_ascii_letter_returns_false():
    # Covers the False branch: len == 1 but ord('é') == 233 > 122
    assert check_if_last_char_is_a_letter("hello é") is False


def test_empty_string_returns_false():
    # "".split(' ') == [''] -> len(check) == 0 -> False
    assert check_if_last_char_is_a_letter("") is False


def test_trailing_space_returns_false():
    # "abc ".split(' ') == ['abc', ''] -> len(check) == 0 -> False
    assert check_if_last_char_is_a_letter("abc ") is False


def test_single_letter_string_returns_true():
    # Whole string is a single letter
    assert check_if_last_char_is_a_letter("a") is True


def test_multiple_spaces_still_takes_last_word():
    # split(' ') on multiple spaces yields empty strings in between;
    # last element is still the final word
    assert check_if_last_char_is_a_letter("hello  world  b") is True
    assert check_if_last_char_is_a_letter("hello  world  bb") is False
