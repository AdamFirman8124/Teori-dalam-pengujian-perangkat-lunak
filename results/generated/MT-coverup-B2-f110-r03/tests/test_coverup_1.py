# file: project/f110/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}

from f110 import exchange


def test_exchange_yes_enough_evens():
    assert exchange([1, 3, 5], [2, 4, 6]) == "YES"


def test_exchange_no_not_enough_evens():
    assert exchange([1, 3, 5, 7], [2, 4]) == "NO"


def test_exchange_empty_lists():
    assert exchange([], []) == "YES"


def test_exchange_no_odds_needs_no_evens():
    # covers False branches of both parity checks: evens in lst1, odds in lst2
    assert exchange([2, 4, 6], [1, 3, 5]) == "YES"


def test_exchange_mixed_parity_yes():
    # lst1 has both odd and even, lst2 has both odd and even
    assert exchange([1, 2, 3], [2, 3, 4]) == "YES"


def test_exchange_mixed_parity_no():
    # lst1 has both odd and even, lst2 has both odd and even but not enough evens
    assert exchange([1, 2, 3, 5], [2, 3, 5]) == "NO"
