# file: project/f089/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

from f089 import encrypt


def test_encrypt_shifts_lowercase_and_preserves_other_characters():
    value = "az by! 123\n"
    assert encrypt(value) == "ed fc! 123\n"


def test_encrypt_returns_empty_string_unchanged():
    assert encrypt("") == ""
