# file: project/f043/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}

from f043 import pairs_sum_to_zero


def test_empty_list_returns_false():
    assert pairs_sum_to_zero([]) is False


def test_single_element_returns_false():
    assert pairs_sum_to_zero([1]) is False


def test_pair_summing_to_zero_returns_true():
    assert pairs_sum_to_zero([1, 3, 5, -3]) is True


def test_no_pair_summing_to_zero_returns_false():
    assert pairs_sum_to_zero([1, 2, 3, 4]) is False


def test_negative_and_positive_pair_returns_true():
    assert pairs_sum_to_zero([-7, 2, 7]) is True


def test_duplicate_zeros_return_true():
    assert pairs_sum_to_zero([0, 0]) is True


def test_single_zero_returns_false():
    assert pairs_sum_to_zero([0]) is False


def test_pair_at_end_of_list_returns_true():
    assert pairs_sum_to_zero([4, 5, 6, -6]) is True


def test_all_negative_returns_false():
    assert pairs_sum_to_zero([-1, -2, -3]) is False


def test_input_list_not_mutated():
    data = [1, -1, 2]
    snapshot = list(data)
    assert pairs_sum_to_zero(data) is True
    assert data == snapshot
