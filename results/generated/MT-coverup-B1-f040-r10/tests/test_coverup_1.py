# file: project/f040/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}

from f040 import triples_sum_to_zero


def test_triples_sum_to_zero_finds_matching_triple():
    assert triples_sum_to_zero([1, 2, -3]) is True


def test_triples_sum_to_zero_checks_all_combinations_without_match():
    assert triples_sum_to_zero([1, 2, 3, 4]) is False


def test_triples_sum_to_zero_with_fewer_than_three_items():
    assert triples_sum_to_zero([1, -1]) is False
