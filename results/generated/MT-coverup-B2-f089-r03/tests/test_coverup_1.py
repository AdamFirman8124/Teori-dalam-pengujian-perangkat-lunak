# file: project/f089/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

from f089 import encrypt


def test_encrypts_lowercase_letters():
    assert encrypt("abcdefghijklmnopqrstuvwxyz") == "efghijklmnopqrstuvwxyzabcd"


def test_preserves_non_lowercase_characters():
    assert encrypt("aZ-09!") == "eZ-09!"
