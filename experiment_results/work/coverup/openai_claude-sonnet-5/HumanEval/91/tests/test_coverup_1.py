# file: script_91.py:1-15
# asked: {"lines": [13, 14, 15], "branches": []}
# gained: {"lines": [13, 14, 15], "branches": []}

import pytest
from script_91 import is_bored


def test_is_bored_no_boredom():
    assert is_bored("Hello world") == 0


def test_is_bored_one_boredom():
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1


def test_is_bored_multiple_boredoms():
    assert is_bored("I am tired. I need sleep. I want rest") == 3


def test_is_bored_question_mark_delimiter():
    assert is_bored("Are you ready? I am ready. What time is it?") == 1


def test_is_bored_exclamation_mark_delimiter():
    assert is_bored("Watch out! I see danger! Run away!") == 1


def test_is_bored_mixed_delimiters():
    assert is_bored("Hello! I am here? I think so. Yes") == 2


def test_is_bored_empty_string():
    assert is_bored("") == 0


def test_is_bored_only_delimiters():
    assert is_bored("...???!!!") == 0


def test_is_bored_i_without_space():
    assert is_bored("Ice cream is good. I love it") == 1


def test_is_bored_lowercase_i_start():
    assert is_bored("i am here. I am there") == 1


def test_is_bored_no_space_after_delimiter():
    assert is_bored("First.I am second.Third") == 1


def test_is_bored_multiple_spaces_after_delimiter():
    assert is_bored("First.    I am second.     I am third") == 2


def test_is_bored_sentence_starting_with_i_only():
    assert is_bored("I") == 0


def test_is_bored_trailing_delimiter():
    assert is_bored("I am bored.") == 1
