# file: project/f110/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}

from f110 import exchange


def test_exchange_returns_yes_when_even_count_is_sufficient():
    assert exchange([1, 2], [2, 3]) == "YES"
    assert exchange([], []) == "YES"


def test_exchange_returns_no_when_even_count_is_insufficient():
    assert exchange([1, 3], [2, 3]) == "NO"
