# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f091 import is_bored


def test_is_bored_single():
    assert is_bored("I am bored.") == 1


def test_is_bored_mixed_delimiters():
    assert is_bored("I love pizza. You love pizza. I hate rain? Are you bored! I am bored.") == 3


def test_is_bored_none_bored():
    assert is_bored("You are bored. He is bored? Are we bored! ") == 0


def test_is_bored_empty_and_no_delimiter():
    assert is_bored("") == 0
    assert is_bored("I am bored") == 1
    assert is_bored("Ice cream is good. I like it.") == 1
