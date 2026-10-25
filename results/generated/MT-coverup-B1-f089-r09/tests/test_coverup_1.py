# file: project/f089/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

from f089 import encrypt


def test_encrypt_shifts_lowercase_letters_by_four():
    plaintext = "abyz"
    assert encrypt(plaintext) == "efcd"


def test_encrypt_preserves_non_lowercase_characters():
    plaintext = "A Z-09!"
    assert encrypt(plaintext) == plaintext
