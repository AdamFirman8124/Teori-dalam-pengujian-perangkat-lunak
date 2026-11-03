# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

"""Tests for f091.is_bored — exercises lines 3-5 (import re, split, sum)."""

import pytest

from f091 import is_bored


def test_is_bored_no_boredom():
    """Sentences not starting with 'I ' yield 0."""
    assert is_bored("Hello world") == 0


def test_is_bored_single_i_sentence():
    """A single sentence starting with 'I ' counts once."""
    assert is_bored("I love it") == 1


def test_is_bored_multiple_delimiters():
    """All of '.', '?' and '!' act as sentence separators."""
    assert is_bored("I am bored! I want to go home? You stay here. I leave now") == 3


def test_is_bored_case_sensitive():
    """Lowercase 'i ' does not count; only capital 'I ' does."""
    assert is_bored("i think so. I think so") == 1


def test_is_bored_empty_and_short():
    """Empty string and very short sentences are handled safely."""
    assert is_bored("") == 0          # split yields ['']
    assert is_bored("I") == 0         # slice 'I' != 'I '
    assert is_bored("I.") == 0        # pieces 'I' and '' both miss


def test_is_bored_delimiter_without_space():
    """Delimiters with no trailing whitespace still split correctly."""
    assert is_bored("I like it.I hate it!Do you?") == 2


def test_is_bored_trailing_delimiter_adds_empty_sentence():
    """A trailing delimiter produces an empty final piece counted as 0."""
    assert is_bored("I am here!") == 1
