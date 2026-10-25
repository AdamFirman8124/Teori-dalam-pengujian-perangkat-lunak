# file: project/f134/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f134 import check_if_last_char_is_a_letter


@pytest.mark.parametrize("letter", ["a", "Z"])
def test_last_character_is_a_letter(letter):
    assert check_if_last_char_is_a_letter(f"Hello {letter}") is True


def test_last_token_has_multiple_characters():
    assert check_if_last_char_is_a_letter("Hello ab") is False


def test_last_character_is_not_a_letter():
    assert check_if_last_char_is_a_letter("Hello ?") is False
