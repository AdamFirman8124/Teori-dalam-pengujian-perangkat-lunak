# file: project/f110/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 8], [6, 5], [6, 7], [8, 9], [8, 11], [9, 8], [9, 10], [11, 12], [11, 13]]}

from f110 import exchange


def test_exchange_returns_yes_when_enough_even_numbers():
    lst1 = [1, 2, 3]
    lst2 = [2, 4, 5]
    originals = (lst1.copy(), lst2.copy())

    assert exchange(lst1, lst2) == "YES"
    assert (lst1, lst2) == originals


def test_exchange_returns_no_when_too_few_even_numbers():
    lst1 = [1, 3]
    lst2 = [2, 5]
    originals = (lst1.copy(), lst2.copy())

    assert exchange(lst1, lst2) == "NO"
    assert (lst1, lst2) == originals
