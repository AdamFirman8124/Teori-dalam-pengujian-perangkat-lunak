# file: project/f089/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

from f089 import encrypt


def test_encrypt_shifts_lowercase_letters_by_four():
    assert encrypt("abcd") == "efgh"
    assert encrypt("xyz") == "bcd"


def test_encrypt_leaves_non_lowercase_chars_unchanged():
    assert encrypt("A1 !") == "A1 !"
    assert encrypt("Hello, World!") == "Hipps, Wsvph!"


def test_encrypt_empty_string():
    assert encrypt("") == ""
