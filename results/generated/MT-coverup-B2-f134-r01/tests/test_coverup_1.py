# file: project/f134/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f134 import check_if_last_char_is_a_letter


def test_last_word_is_single_lowercase_letter():
    # Covers the True branch: len(check) == 1 and 97 <= ord <= 122
    assert check_if_last_char_is_a_letter("hello worl d") is True


def test_last_word_is_single_uppercase_letter():
    # Uppercase letter is lowered before the ord check, so still True
    assert check_if_last_char_is_a_letter("hello worl D") is True


def test_last_word_is_single_digit():
    # Covers False branch: len(check) == 1 but ord('1') == 49 < 97
    assert check_if_last_char_is_a_letter("hello worl 1") is False


def test_last_word_is_single_char_above_z():
    # Covers False branch: len(check) == 1 but ord('{') == 123 > 122
    assert check_if_last_char_is_a_letter("hello worl {") is False


def test_last_word_is_longer_than_one_char():
    # Covers False branch: len(check) != 1 (short-circuits before ord)
    assert check_if_last_char_is_a_letter("hello world") is False


def test_empty_string():
    # "".split(' ') == [''] -> len(check) == 0 -> False
    assert check_if_last_char_is_a_letter("") is False


def test_trailing_space():
    # "hello ".split(' ') == ['hello', ''] -> len(check) == 0 -> False
    assert check_if_last_char_is_a_letter("hello ") is False
