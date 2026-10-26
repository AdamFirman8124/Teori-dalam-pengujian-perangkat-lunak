# file: project/f014/__init__.py:4-10
# asked: {"lines": [6, 8, 9, 10], "branches": [[8, 9], [8, 10]]}
# gained: {"lines": [6, 8, 9, 10], "branches": [[8, 9], [8, 10]]}

import pytest

from f014 import all_prefixes


def test_all_prefixes_nonempty():
    result = all_prefixes("abc")
    assert result == ["a", "ab", "abc"]
    assert len(result) == len("abc")


def test_all_prefixes_single_char():
    result = all_prefixes("x")
    assert result == ["x"]


def test_all_prefixes_empty_string():
    result = all_prefixes("")
    assert result == []
