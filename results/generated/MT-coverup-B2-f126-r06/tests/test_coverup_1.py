# file: project/f126/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}

from f126 import is_sorted


def test_is_sorted_rejects_values_repeated_more_than_twice():
    assert is_sorted([1, 1, 1]) is False


def test_is_sorted_accepts_sorted_values_with_at_most_two_duplicates():
    assert is_sorted([1, 1, 2, 2, 3]) is True


def test_is_sorted_rejects_unsorted_values():
    assert is_sorted([1, 3, 2]) is False
