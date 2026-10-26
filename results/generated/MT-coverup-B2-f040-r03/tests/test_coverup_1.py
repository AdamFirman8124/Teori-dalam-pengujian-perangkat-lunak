# file: project/f040/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}

from f040 import triples_sum_to_zero


def test_empty_list_returns_false():
    assert triples_sum_to_zero([]) is False


def test_single_element_returns_false():
    assert triples_sum_to_zero([0]) is False


def test_two_elements_returns_false():
    assert triples_sum_to_zero([1, -1]) is False


def test_three_elements_no_zero_sum_returns_false():
    assert triples_sum_to_zero([1, 2, 3]) is False


def test_three_elements_zero_sum_returns_true():
    assert triples_sum_to_zero([-1, 0, 1]) is True


def test_all_zeros_returns_true():
    assert triples_sum_to_zero([0, 0, 0]) is True


def test_zero_sum_triple_later_in_list_returns_true():
    # First triples do not sum to zero; only last triple (1, 2, -3) does,
    # forcing full iteration of i/j/k loops before returning True.
    assert triples_sum_to_zero([5, 1, 2, -3]) is True


def test_longer_list_no_zero_sum_returns_false():
    assert triples_sum_to_zero([1, 2, 4, 8, 16]) is False
