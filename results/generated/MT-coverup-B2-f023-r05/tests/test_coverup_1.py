# file: project/f023/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f023 import strlen


def test_strlen_empty():
    assert strlen("") == 0


def test_strlen_ascii():
    assert strlen("hello") == 5


def test_strlen_unicode():
    assert strlen("héllo 🌍") == 7
