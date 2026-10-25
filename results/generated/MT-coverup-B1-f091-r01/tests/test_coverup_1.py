# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f091 import is_bored


def test_is_bored_counts_sentences_starting_with_i():
    assert is_bored("I am bored. Are you? I want cake!") == 2


def test_is_bored_returns_zero_when_no_sentence_starts_with_i():
    assert is_bored("You are bored. I'm not!") == 0
