# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f091 import is_bored


def test_is_bored_no_bored_sentences():
    # Single sentence not starting with 'I '
    assert is_bored("Hello world") == 0


def test_is_bored_one_bored_sentence():
    # Classic example: only one sentence starts with 'I '
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1


def test_is_bored_multiple_bored_sentences_all_delimiters():
    # Covers '.', '?' and '!' delimiters, each followed by whitespace
    assert is_bored("I am bored! I want to go home? I hate this. You are boring") == 3


def test_is_bored_empty_string():
    # Empty input splits into a single empty sentence, which does not start with 'I '
    assert is_bored("") == 0


def test_is_bored_I_without_following_space():
    # 'It' starts with 'I' but not with 'I ' (I followed by a space)
    assert is_bored("It is raining. I am sad") == 1


def test_is_bored_delimiter_without_trailing_space():
    # The regex allows zero whitespace after the delimiter
    assert is_bored("I am tired.I need sleep") == 2
