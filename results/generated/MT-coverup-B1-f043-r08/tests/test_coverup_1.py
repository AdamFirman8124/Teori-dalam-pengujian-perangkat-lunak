# file: project/f043/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 7], [4, 3], [4, 5], [5, 4], [5, 6]]}

from f043 import pairs_sum_to_zero


def test_pairs_sum_to_zero_returns_true_for_opposite_pair():
    assert pairs_sum_to_zero([3, 1, -3]) is True


def test_pairs_sum_to_zero_returns_false_without_opposite_pair():
    assert pairs_sum_to_zero([1, 2, 3]) is False
