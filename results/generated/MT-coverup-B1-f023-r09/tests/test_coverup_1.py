# file: project/f023/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f023 import strlen


def test_strlen_empty():
    assert strlen("") == 0


def test_strlen_basic():
    assert strlen("hello") == 5


def test_strlen_unicode_and_spaces():
    assert strlen("a b") == 3
    assert strlen("héllo") == 5
