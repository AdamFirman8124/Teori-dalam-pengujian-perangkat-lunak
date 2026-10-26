# file: project/f080/__init__.py:1-10
# asked: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}

import pytest

from f080 import is_happy


def test_is_happy_returns_false_for_short_strings():
    assert is_happy("") is False
    assert is_happy("a") is False
    assert is_happy("ab") is False


def test_is_happy_returns_true_when_all_triples_are_distinct():
    assert is_happy("abc") is True
    assert is_happy("abcd") is True
    assert is_happy("abcdefg") is True


def test_is_happy_returns_false_when_adjacent_pair_repeats():
    # s[i] == s[i + 1]
    assert is_happy("aab") is False
    assert is_happy("abbc") is False


def test_is_happy_returns_false_when_outer_pair_repeats():
    # s[i] == s[i + 2]
    assert is_happy("aba") is False
    assert is_happy("abac") is False


def test_is_happy_returns_false_when_trailing_pair_repeats():
    # s[i + 1] == s[i + 2]
    assert is_happy("abcc") is False
    assert is_happy("abcdd") is False


def test_is_happy_checks_every_window_not_just_the_first():
    # First windows are fine, a later window repeats.
    assert is_happy("abcdeff") is False
    assert is_happy("abcdaa") is False
    assert is_happy("abcdbc") is True


def test_is_happy_does_not_mutate_input():
    s = "abcdef"
    assert is_happy(s) is True
    assert s == "abcdef"
