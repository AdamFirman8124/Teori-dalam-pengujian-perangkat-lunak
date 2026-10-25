# file: project/f134/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f134 import check_if_last_char_is_a_letter


def test_last_character_is_a_letter():
    assert check_if_last_char_is_a_letter("Is it A") is True


def test_last_token_has_multiple_characters():
    assert check_if_last_char_is_a_letter("This is false") is False


def test_last_character_is_not_a_letter():
    assert check_if_last_char_is_a_letter("Is it 1") is False
