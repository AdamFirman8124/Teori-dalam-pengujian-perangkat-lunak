# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f091 import is_bored


def test_single_bored_sentence():
    assert is_bored("I am bored. You are not.") == 1


def test_multiple_bored_sentences():
    assert is_bored("I love pizza! I hate rain? I am bored.") == 3


def test_no_bored_sentences():
    assert is_bored("Hello world. You are great! Are you ok?") == 0


def test_empty_string():
    assert is_bored("") == 0


def test_bored_exact_and_short_strings():
    assert is_bored("I ") == 1
    assert is_bored("I") == 0
    assert is_bored("I am bored.") == 1


def test_leading_space_is_not_bored():
    # sentence[0:2] == 'I ' is False when there is a leading space
    assert is_bored(" I am bored.") == 0
    assert is_bored("I am bored. I am tired. You are awake.") == 2
