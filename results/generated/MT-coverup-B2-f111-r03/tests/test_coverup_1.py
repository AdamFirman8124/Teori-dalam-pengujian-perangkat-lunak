# file: project/f111/__init__.py:1-15
# asked: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}

"""Tests for f111.histogram — full line and branch coverage.

The function is pure (no I/O, no module state), so no monkeypatching or
cleanup is required; each test is self-contained and side-effect free.
"""

from f111 import histogram


def test_histogram_empty_string():
    """Empty input: the only token is '', which is skipped, so t stays 0.

    Covers: lines 3-9, the False branch of `i != ''` (line 8),
    the False branch of `if t > 0` (line 10), and the return (line 15).
    """
    assert histogram("") == {}


def test_histogram_single_most_frequent_word():
    """One word dominates: only that word is reported with its count.

    Covers: True branch of line 8 (first 'a'), False branch of line 8
    via count not exceeding t (second 'a'), True branch of line 10,
    True branch of line 12 ('a'), False branch of line 12 ('b'),
    and the dict assignment on line 14.
    """
    assert histogram("a b a") == {"a": 2}


def test_histogram_tie_between_words():
    """Several words tie for the maximum count: all of them are reported."""
    assert histogram("a b a b") == {"a": 2, "b": 2}


def test_histogram_single_word():
    """A single word with no spaces yields a count of 1."""
    assert histogram("hello") == {"hello": 1}


def test_histogram_ignores_empty_tokens_but_still_finds_max():
    """Leading/trailing spaces create '' tokens that are skipped, yet a
    positive maximum still exists, exercising the False branch of
    `i != ''` together with the True branch of `if t > 0`."""
    assert histogram("  a b  ") == {"a": 1, "b": 1}
