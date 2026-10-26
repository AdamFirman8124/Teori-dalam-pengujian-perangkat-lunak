# file: project/f126/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}

from f126 import is_sorted


def test_empty_list_is_sorted():
    assert is_sorted([]) is True


def test_single_element_is_sorted():
    assert is_sorted([5]) is True


def test_sorted_list_returns_true():
    assert is_sorted([1, 2, 3, 4]) is True


def test_sorted_with_double_occurrence_returns_true():
    assert is_sorted([1, 2, 2, 3]) is True


def test_triple_occurrence_returns_false():
    assert is_sorted([1, 1, 1]) is False


def test_triple_occurrence_at_end_returns_false():
    assert is_sorted([1, 2, 3, 3, 3]) is False


def test_unsorted_without_triple_returns_false():
    assert is_sorted([3, 1, 2]) is False


def test_unsorted_with_double_occurrence_returns_false():
    assert is_sorted([1, 3, 2, 2]) is False
