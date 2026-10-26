# file: project/f072/__init__.py:1-12
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11, 12], "branches": [[3, 4], [3, 6], [7, 8], [7, 12], [8, 9], [8, 10]]}

from f072 import will_it_fly


def test_sum_exceeds_w_returns_false():
    assert will_it_fly([5, 5, 5], 10) is False
    assert will_it_fly([1, 2, 3], 5) is False


def test_sum_equal_w_palindrome_returns_true():
    assert will_it_fly([1, 2, 1], 4) is True
    assert will_it_fly([2, 2], 4) is True


def test_odd_palindrome_within_w_returns_true():
    assert will_it_fly([1, 2, 1], 10) is True
    assert will_it_fly([1, 2, 3, 2, 1], 10) is True


def test_even_palindrome_within_w_returns_true():
    assert will_it_fly([1, 2, 2, 1], 10) is True


def test_empty_and_single_element_return_true():
    assert will_it_fly([], 0) is True
    assert will_it_fly([1], 1) is True
    assert will_it_fly([3], 5) is True


def test_non_palindrome_within_w_returns_false_first_pair():
    assert will_it_fly([1, 2, 3], 10) is False
    assert will_it_fly([1, 2], 5) is False


def test_non_palindrome_mismatch_on_second_iteration_returns_false():
    # first pair matches (1==1), second pair mismatches (2!=1)
    assert will_it_fly([1, 2, 3, 1, 1], 20) is False
