# file: project/f089/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

from f089 import encrypt


def test_encrypt_shifts_lowercase_letters_and_preserves_other_characters():
    assert encrypt("abcxyz ABC 123!") == "efgbcd ABC 123!"


def test_encrypt_returns_empty_input_unchanged():
    assert encrypt("") == ""
