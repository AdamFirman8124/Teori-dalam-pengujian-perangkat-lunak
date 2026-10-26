# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f091 import is_bored


def test_is_bored_counts_sentences_starting_with_I():
    assert is_bored("I love pizza. I hate rain! Do you? I do.") == 3


def test_is_bored_no_boredom():
    assert is_bored("The sky is blue. The sun is shining.") == 0


def test_is_bored_empty_string():
    assert is_bored("") == 0


def test_is_bored_various_separators():
    assert is_bored("I am bored?I am not! I am. You are") == 3


def test_is_bored_lowercase_i_not_counted():
    assert is_bored("i am bored. I am not.") == 1


def test_is_bored_I_alone_not_counted():
    assert is_bored("I. I am.") == 1
