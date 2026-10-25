# file: project/f104/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f104 import unique_digits


def test_unique_digits_empty():
    assert unique_digits([]) == []


def test_unique_digits_all_odd_unsorted_returns_sorted():
    assert unique_digits([77, 5, 13, 31]) == [5, 13, 31, 77]


def test_unique_digits_mixed_keeps_only_all_odd():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]


def test_unique_digits_none_qualify():
    assert unique_digits([10, 152, 323, 246, 8, 20]) == []
