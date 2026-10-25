# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f091 import is_bored


def test_is_bored_counts_bored_sentences():
    # Multiple sentences, some starting with "I "
    assert is_bored("I love pizza. The sky is blue. I am happy!") == 2


def test_is_bored_empty_string():
    # Empty string: re.split still runs, returns [''], sum is 0
    assert is_bored("") == 0


def test_is_bored_no_bored_sentences():
    # No sentence starts with "I "
    assert is_bored("Hello world. How are you?") == 0


def test_is_bored_various_delimiters():
    # Delimiters . ? ! with and without trailing whitespace
    assert is_bored("I am here?I am there!I see. We go") == 3


def test_is_bored_trailing_delimiter():
    # Trailing delimiter produces an empty final sentence; must not crash
    assert is_bored("I like it.") == 1


def test_is_bored_i_without_space_not_counted():
    # "It" starts with 'I' but not 'I ' (sentence[0:2] == 'I ' is False)
    assert is_bored("It is fine. I am fine.") == 1
