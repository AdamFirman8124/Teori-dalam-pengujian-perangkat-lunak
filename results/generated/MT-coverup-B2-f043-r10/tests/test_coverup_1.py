# file: project/f043/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}

from f043 import pairs_sum_to_zero


def test_empty_list_returns_false():
    assert pairs_sum_to_zero([]) is False


def test_single_element_returns_false():
    assert pairs_sum_to_zero([1]) is False
    assert pairs_sum_to_zero([0]) is False


def test_direct_pair_sums_to_zero():
    assert pairs_sum_to_zero([1, -1]) is True
    assert pairs_sum_to_zero([0, 0]) is True


def test_no_pair_sums_to_zero():
    assert pairs_sum_to_zero([1, 2, 3]) is False
    assert pairs_sum_to_zero([1, 2, 3, 4]) is False


def test_pair_found_after_failed_inner_iterations():
    # first inner check fails, second succeeds on same outer iteration
    assert pairs_sum_to_zero([5, 3, -5, 1]) is True
    # first outer iteration all fail, success on second outer iteration
    assert pairs_sum_to_zero([1, 2, -2]) is True


def test_pair_found_on_later_outer_iteration():
    assert pairs_sum_to_zero([1, 2, 3, -3]) is True
    assert pairs_sum_to_zero([-4, 1, 2, 4]) is True
