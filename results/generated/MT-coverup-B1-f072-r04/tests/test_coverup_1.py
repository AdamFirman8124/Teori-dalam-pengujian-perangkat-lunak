# file: project/f072/__init__.py:1-12
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}

from f072 import will_it_fly


def test_sum_exceeds_w_returns_false():
    assert will_it_fly([5, 5, 5], 10) is False
    assert will_it_fly([10, 1], 5) is False


def test_empty_list_returns_true():
    assert will_it_fly([], 0) is True
    assert will_it_fly([], 10) is True


def test_single_element_returns_true():
    assert will_it_fly([1], 1) is True
    assert will_it_fly([3], 5) is True


def test_odd_palindrome_within_limit_returns_true():
    assert will_it_fly([1, 2, 1], 5) is True
    assert will_it_fly([1, 2, 1], 4) is True


def test_even_palindrome_multi_iteration_returns_true():
    assert will_it_fly([1, 2, 2, 1], 10) is True
    assert will_it_fly([3, 2, 2, 3], 10) is True


def test_non_palindrome_first_pair_returns_false():
    assert will_it_fly([1, 2, 3], 10) is False
    assert will_it_fly([1, 2, 2, 3], 10) is False


def test_non_palindrome_inner_pair_returns_false():
    assert will_it_fly([1, 2, 3, 4, 1], 20) is False
    assert will_it_fly([1, 2, 3, 2, 0], 20) is False
