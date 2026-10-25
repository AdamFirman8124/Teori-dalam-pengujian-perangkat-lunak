# file: project/f040/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}

from f040 import triples_sum_to_zero


def test_triples_sum_to_zero_finds_zero_sum_triple():
    assert triples_sum_to_zero([1, 2, -3]) is True


def test_triples_sum_to_zero_returns_false_when_no_triple_matches():
    assert triples_sum_to_zero([1, 2, 4, 8]) is False
