# file: project/f134/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f134 import check_if_last_char_is_a_letter


def test_last_word_single_lowercase_letter_returns_true():
    assert check_if_last_char_is_a_letter("apple pie a") is True
    assert check_if_last_char_is_a_letter("apple pi e") is True
    assert check_if_last_char_is_a_letter("a") is True
    assert check_if_last_char_is_a_letter("z") is True


def test_last_word_single_uppercase_letter_returns_true():
    assert check_if_last_char_is_a_letter("apple pie A") is True
    assert check_if_last_char_is_a_letter("apple pie Z") is True
    assert check_if_last_char_is_a_letter("A") is True


def test_last_word_multi_char_returns_false():
    assert check_if_last_char_is_a_letter("apple pie") is False
    assert check_if_last_char_is_a_letter("apple pi e ") is False
    assert check_if_last_char_is_a_letter("apple!") is False
    assert check_if_last_char_is_a_letter("ab") is False


def test_last_word_single_digit_returns_false():
    assert check_if_last_char_is_a_letter("apple 1") is False
    assert check_if_last_char_is_a_letter("1") is False


def test_last_word_single_char_below_a_returns_false():
    # ord("`") == 96, ord("!") == 33, both < 97
    assert check_if_last_char_is_a_letter("apple `") is False
    assert check_if_last_char_is_a_letter("apple !") is False


def test_last_word_single_char_above_z_returns_false():
    # ord("{") == 123 > 122, covers second half of chained comparison False
    assert check_if_last_char_is_a_letter("apple {") is False
    assert check_if_last_char_is_a_letter("{") is False


def test_empty_and_blank_strings_return_false():
    assert check_if_last_char_is_a_letter("") is False
    assert check_if_last_char_is_a_letter(" ") is False
    assert check_if_last_char_is_a_letter("apple a ") is False
