# file: project/f023/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f023 import strlen


def test_strlen_empty_string():
    result = strlen("")
    assert result == 0
    assert isinstance(result, int)


def test_strlen_single_character():
    result = strlen("a")
    assert result == 1
    assert isinstance(result, int)


def test_strlen_typical_string():
    result = strlen("hello")
    assert result == 5
    assert isinstance(result, int)


def test_strlen_string_with_spaces_and_punctuation():
    result = strlen("hello world!")
    assert result == 12
    assert isinstance(result, int)


def test_strlen_unicode_string():
    result = strlen("héllo")
    assert result == 5
    assert isinstance(result, int)
