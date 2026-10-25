# file: project/f012/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 0], [10, 11], [11, 10], [11, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 11], [11, 10], [11, 12]]}

from f012 import longest


def test_longest_returns_none_for_empty_list():
    assert longest([]) is None


def test_longest_returns_first_longest_string():
    strings = ["a", "longest", "bb", "sameone"]
    assert longest(strings) == "longest"
