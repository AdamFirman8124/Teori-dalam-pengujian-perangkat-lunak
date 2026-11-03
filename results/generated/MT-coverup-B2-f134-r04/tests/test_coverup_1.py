# file: project/f134/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f134 import check_if_last_char_is_a_letter


def test_last_char_is_lowercase_letter():
    # Last word is a single lowercase letter -> True branch taken
    assert check_if_last_char_is_a_letter("hello a") is True


def test_last_char_is_uppercase_letter():
    # Uppercase letter is lowered before the ord check -> still True
    assert check_if_last_char_is_a_letter("hello Z") is True


def test_last_char_is_digit():
    # Single char but not a letter -> False via the ord range check
    assert check_if_last_char_is_a_letter("hello 1") is False


def test_last_word_longer_than_one_char():
    # Last word has more than one char -> False via the len check (short-circuits ord)
    assert check_if_last_char_is_a_letter("hello ab") is False


def test_empty_string():
    # split('') yields [''], len 0 -> False via the len check
    assert check_if_last_char_is_a_letter("") is False


def test_single_word_no_space():
    # No spaces: whole word is the last element, len > 1 -> False
    assert check_if_last_char_is_a_letter("hello") is False


def test_trailing_space():
    # Trailing space makes the last split element an empty string -> False
    assert check_if_last_char_is_a_letter("hello a ") is False
