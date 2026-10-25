# file: project/f134/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f134 import check_if_last_char_is_a_letter


def test_check_if_last_char_is_a_letter_accepts_letters():
    assert check_if_last_char_is_a_letter("a") is True
    assert check_if_last_char_is_a_letter("ends with Z") is True


def test_check_if_last_char_is_a_letter_rejects_nonletters():
    assert check_if_last_char_is_a_letter("ab") is False
    assert check_if_last_char_is_a_letter("1") is False
    assert check_if_last_char_is_a_letter("{") is False
    assert check_if_last_char_is_a_letter("trailing space ") is False
