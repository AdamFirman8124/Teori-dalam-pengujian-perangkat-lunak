# file: project/f014/__init__.py:4-10
# asked: {"lines": [6, 8, 9, 10], "branches": [[8, 9], [8, 10]]}
# gained: {"lines": [6, 8, 9, 10], "branches": [[8, 9], [8, 10]]}

from f014 import all_prefixes


def test_all_prefixes_returns_each_prefix():
    assert all_prefixes("abc") == ["a", "ab", "abc"]


def test_all_prefixes_returns_empty_list_for_empty_string():
    assert all_prefixes("") == []
