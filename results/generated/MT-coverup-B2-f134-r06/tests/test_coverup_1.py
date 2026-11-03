# file: project/f134/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f134 import check_if_last_char_is_a_letter


def test_last_word_is_single_lowercase_letter():
    # Exercises line 3 (split) and the True branch of line 4.
    assert check_if_last_char_is_a_letter("hello a") is True


def test_last_word_is_single_uppercase_letter():
    # Uppercase letter is lowercased before the ord() check -> still True.
    assert check_if_last_char_is_a_letter("hello Z") is True


def test_last_word_is_single_non_letter():
    # len(check) == 1 but ord() outside a-z range -> False branch of line 4.
    assert check_if_last_char_is_a_letter("hello 7") is False


def test_last_word_has_multiple_characters():
    # len(check) != 1 short-circuits the 'and' -> False branch of line 4.
    assert check_if_last_char_is_a_letter("hello ab") is False


def test_trailing_space_yields_empty_last_word():
    # "hello ".split(' ')[-1] == "" -> len 0 -> False.
    assert check_if_last_char_is_a_letter("hello ") is False


def test_empty_string():
    # "".split(' ')[-1] == "" -> len 0 -> False.
    assert check_if_last_char_is_a_letter("") is False


def test_single_word_input():
    # No spaces: the only word is also the last one.
    assert check_if_last_char_is_a_letter("a") is True
    assert check_if_last_char_is_a_letter("ab") is False


def test_ord_boundaries():
    # Characters just outside the a-z range -> False.
    assert check_if_last_char_is_a_letter("x " + chr(96)) is False   # '`' -> 96
    assert check_if_last_char_is_a_letter("x " + chr(123)) is False  # '{' -> 123
    # Characters exactly at the a-z boundaries -> True.
    assert check_if_last_char_is_a_letter("x a") is True             # 97
    assert check_if_last_char_is_a_letter("x z") is True             # 122
