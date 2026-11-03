# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f091 import is_bored


def test_is_bored_no_bored_sentences():
    """Covers lines 3-5: import re, split, and sum with no matches."""
    assert is_bored("Hello world") == 0


def test_is_bored_single_bored_sentence():
    """One sentence starts with 'I ' among several."""
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1


def test_is_bored_multiple_bored_sentences():
    """All delimiters (. ? !) are exercised, plus trailing empty split piece."""
    assert is_bored("I am bored! I want to sleep? I dream of cheese.") == 3


def test_is_bored_empty_string():
    """Edge case: empty input yields a single empty sentence, not bored."""
    assert is_bored("") == 0


def test_is_bored_bare_I():
    """Edge case: bare 'I' without trailing space does not count."""
    assert is_bored("I") == 0


def test_is_bored_I_without_space_after_delimiter():
    """'I' immediately followed by a non-space character must not count.

    Note: the delimiter regex consumes the '.' and any following whitespace,
    so in "Hi.Ilike it" the second sentence is 'Ilike it', which does not
    start with 'I ' and therefore is not counted.
    """
    assert is_bored("Hi.Ilike it") == 0


def test_is_bored_I_after_delimiter_without_space_counts():
    """The delimiter regex eats following whitespace, so 'I ' after '.' counts."""
    assert is_bored("Hi.I am fine") == 1


def test_is_bored_is_pure():
    """The function must not mutate its input (no state pollution)."""
    s = "I like it. You like it!"
    original = s
    assert is_bored(s) == 1
    assert s == original
