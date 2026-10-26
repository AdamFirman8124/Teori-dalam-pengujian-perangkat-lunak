# file: project/f134/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f134 import check_if_last_char_is_a_letter


def test_last_char_is_single_lowercase_letter_returns_true():
    result = check_if_last_char_is_a_letter("hello a")
    assert result is True


def test_last_char_is_single_uppercase_letter_returns_true():
    result = check_if_last_char_is_a_letter("hello A")
    assert result is True


def test_last_char_is_multiple_letters_returns_false():
    result = check_if_last_char_is_a_letter("hello ab")
    assert result is False


def test_last_char_is_single_digit_returns_false():
    result = check_if_last_char_is_a_letter("hello 1")
    assert result is False


def test_last_char_is_single_non_alpha_symbol_returns_false():
    result = check_if_last_char_is_a_letter("hello !")
    assert result is False


def test_trailing_space_yields_empty_last_token_returns_false():
    result = check_if_last_char_is_a_letter("hello ")
    assert result is False


def test_empty_string_returns_false():
    result = check_if_last_char_is_a_letter("")
    assert result is False


def test_single_letter_only_returns_true():
    result = check_if_last_char_is_a_letter("z")
    assert result is True


@pytest.mark.parametrize(
    "txt, expected",
    [
        ("a", True),
        ("Z", True),
        ("ab", False),
        ("a b", True),
        ("a bc", False),
        ("a 1", False),
        ("a ", False),
        ("", False),
    ],
)
def test_return_type_is_strict_bool(txt, expected):
    result = check_if_last_char_is_a_letter(txt)
    assert result is expected
    assert isinstance(result, bool)
