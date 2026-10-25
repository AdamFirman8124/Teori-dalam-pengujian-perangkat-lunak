# file: project/f012/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 0], [10, 11], [11, 10], [11, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 11], [11, 10], [11, 12]]}

from f012 import longest


def test_longest_empty_list_returns_none():
    assert longest([]) is None


def test_longest_returns_first_longest_string():
    assert longest(["a", "longest", "xyz", "another"]) == "longest"


def test_longest_handles_tied_lengths():
    assert longest(["first", "other", "x"]) == "first"
