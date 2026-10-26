# file: project/f089/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import f089


def test_encrypt_shifts_lowercase_letters_and_preserves_other_characters():
    result = f089.encrypt("abcxyz A-19")

    assert result == "efgbcd A-19"


def test_encrypt_returns_empty_string_for_empty_input():
    assert f089.encrypt("") == ""
