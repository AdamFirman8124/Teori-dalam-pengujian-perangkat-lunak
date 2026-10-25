# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f091 import is_bored


def test_empty_string():
    assert is_bored("") == 0


def test_single_bored_sentence_with_period():
    assert is_bored("I am bored.") == 1


def test_single_bored_sentence_without_punctuation():
    assert is_bored("I am here") == 1


def test_no_bored_sentences():
    assert is_bored("Hello world. You are great! How are you?") == 0


def test_multiple_mixed_sentences():
    assert is_bored("I love pizza. You love pizza? I hate pizza!") == 2


def test_question_and_exclamation_bored():
    assert is_bored("I am here? I am there! You are here.") == 2


def test_i_without_trailing_space_is_not_bored():
    assert is_bored("I'm bored.") == 0
    assert is_bored("Iam bored.") == 0
    assert is_bored("I") == 0


def test_leading_space_is_not_bored():
    assert is_bored(" I am bored.") == 0
