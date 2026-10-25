# file: project/f134/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f134 import check_if_last_char_is_a_letter


def test_last_char_single_lowercase_letter_true():
    assert check_if_last_char_is_a_letter("apple pie a") is True


def test_last_char_single_uppercase_letter_true():
    assert check_if_last_char_is_a_letter("hello Z") is True


def test_last_char_multi_char_word_false():
    assert check_if_last_char_is_a_letter("apple pie ap") is False


def test_last_char_single_digit_false():
    assert check_if_last_char_is_a_letter("hello 1") is False


def test_last_char_trailing_space_empty_false():
    assert check_if_last_char_is_a_letter("hello ") is False


def test_last_char_symbol_after_z_false():
    assert check_if_last_char_is_a_letter("hello {") is False


def test_last_char_empty_string_false():
    assert check_if_last_char_is_a_letter("") is False
