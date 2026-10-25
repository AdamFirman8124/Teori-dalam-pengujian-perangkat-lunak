# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f091 import is_bored


def test_is_bored_counts_bored_sentences():
    assert is_bored("I love pizza. The sky is blue. I am bored!") == 2


def test_is_bored_no_bored_sentences():
    assert is_bored("You are great? We are happy.") == 0


def test_is_bored_empty_string():
    assert is_bored("") == 0


def test_is_bored_multiple_delimiters():
    assert is_bored("I am here?I am there!I am everywhere.") == 3
