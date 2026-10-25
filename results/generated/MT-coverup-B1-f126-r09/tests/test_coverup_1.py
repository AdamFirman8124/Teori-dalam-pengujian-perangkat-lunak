# file: project/f126/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}

from f126 import is_sorted


def test_is_sorted_returns_false_for_value_repeated_more_than_twice():
    values = [1, 1, 1]
    original = values.copy()

    assert is_sorted(values) is False
    assert values == original


def test_is_sorted_returns_true_for_sorted_values():
    values = [1, 1, 2, 2, 3]
    original = values.copy()

    assert is_sorted(values) is True
    assert values == original


def test_is_sorted_returns_false_for_unsorted_values():
    values = [1, 3, 2]
    original = values.copy()

    assert is_sorted(values) is False
    assert values == original
