# file: project/f012/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 0], [10, 11], [11, 10], [11, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 11], [11, 10], [11, 12]]}

import pytest

from f012 import longest


def test_longest_empty_list_returns_none():
    assert longest([]) is None


def test_longest_single_element():
    assert longest(["abc"]) == "abc"


def test_longest_returns_first_of_equal_lengths():
    assert longest(["aa", "bb", "c"]) == "aa"


def test_longest_skips_shorter_strings_before_match():
    # exercises the False branch of `if len(s) == maxlen` before the True branch
    assert longest(["a", "bb", "ccc", "dd"]) == "ccc"


def test_longest_with_empty_strings():
    assert longest(["", ""]) == ""
    assert longest(["", "x"]) == "x"


def test_longest_does_not_mutate_input(monkeypatch):
    data = ["a", "bbb", "cc"]
    snapshot = list(data)
    assert longest(data) == "bbb"
    assert data == snapshot
