# file: project/f040/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}

from f040 import triples_sum_to_zero


def test_triples_sum_to_zero_returns_true_when_zero_sum_triple_exists():
    values = [1, -1, 0]

    assert triples_sum_to_zero(values) is True


def test_triples_sum_to_zero_returns_false_when_no_zero_sum_triple_exists():
    values = [1, 2, 3, 4]

    assert triples_sum_to_zero(values) is False
