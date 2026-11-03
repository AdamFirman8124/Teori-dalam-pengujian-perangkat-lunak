# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import re

import pytest

from f091 import is_bored


def test_is_bored_counts_sentences_starting_with_i():
    # Lines 3-5: import re, split, and sum the generator over both branches
    assert is_bored("I love tacos. You do too? I like them!") == 2


def test_is_bored_no_i_sentences():
    # All generator outcomes are False -> sum is 0
    assert is_bored("Hello world. How are you? Fine, thanks.") == 0


def test_is_bored_empty_string():
    # re.split(r'[.?!]\s*', '') yields ['']; ''[0:2] != 'I '
    assert is_bored("") == 0


def test_is_bored_delimiters_without_trailing_space():
    # \s* allows zero whitespace after delimiters; still splits
    assert is_bored("I am here!Me too.I said so?") == 2


def test_is_bored_trailing_delimiter_produces_empty_sentence():
    # Splitting yields empty sentences, which must not be counted
    assert is_bored("I am here.. I am there.") == 2


def test_is_bored_lone_i_not_counted():
    # 'I'[0:2] == 'I' which is not 'I '
    assert is_bored("I") == 0


def test_is_bored_i_prefix_word_not_counted():
    assert is_bored("It is fine. I am fine.") == 1


def test_is_bored_leading_space_not_counted():
    # ' I'[0:2] == ' I' != 'I '
    assert is_bored(" I am here. I am there.") == 1


def test_is_bored_calls_re_split(monkeypatch):
    # Spy on re.split to prove lines 3-4 execute with the expected pattern
    calls = []
    original_split = re.split

    def fake_split(pattern, string):
        calls.append((pattern, string))
        return original_split(pattern, string)

    monkeypatch.setattr(re, "split", fake_split)

    result = is_bored("I win. I lose?")

    assert result == 2
    assert calls == [(r'[.?!]\s*', "I win. I lose?")]


def test_is_bored_mixed_delimiters_and_branches():
    # Splits into: 'I am', 'I am', ' no', 'It is', ''
    # Exercises True and False outcomes of the generator in one call
    assert is_bored("I am. I am? no. It is.") == 2
