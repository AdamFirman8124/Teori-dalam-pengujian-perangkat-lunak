# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

"""Tests for f091.is_bored.

The function is pure (no I/O, no global state), so no monkeypatching or
teardown is required; each test simply calls the function and asserts on
its return value, which drives execution of lines 3-5 (the re import,
the re.split call, and the summing generator with both True/False
comparison branches).
"""

import pytest

from f091 import is_bored


def test_is_bored_counts_sentences_starting_with_i():
    # Sentences split on '!' and '.': ['I love It ', 'I hate it now', '']
    # Two start with 'I ', the trailing empty string does not.
    assert is_bored("I love It ! I hate it now.") == 2


def test_is_bored_no_sentence_starts_with_i():
    # 'I' appears but never at the start of a sentence.
    assert is_bored("You and I are going for a walk") == 0


def test_is_bored_empty_string():
    # re.split on '' yields [''], whose slice '' != 'I ' -> 0.
    assert is_bored("") == 0


def test_is_bored_question_and_exclamation_separators():
    # Exercises '?' and '!' separators: ['I am', 'I was', 'He is', '']
    assert is_bored("I am? I was! He is.") == 2


def test_is_bored_prefix_must_be_exactly_i_space():
    # 'It ...' must NOT count; only 'I ' counts. Covers the False branch
    # for a non-empty sentence as well.
    assert is_bored("It is fine. I am not.") == 1


def test_is_bored_multiple_spaces_after_punctuation():
    # r'[.?!]\s*' consumes all whitespace after the punctuation.
    assert is_bored("I am bored.    I am tired?") == 2


def test_is_bored_returns_int_type():
    result = is_bored("I like turtles.")
    assert isinstance(result, int)
    assert result == 1
