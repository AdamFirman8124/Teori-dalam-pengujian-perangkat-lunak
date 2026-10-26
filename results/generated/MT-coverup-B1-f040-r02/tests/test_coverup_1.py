# file: project/f040/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 8], [4, 3], [4, 5], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest

from f040 import triples_sum_to_zero


def test_triples_sum_to_zero_true():
    # 1 + 2 - 3 == 0 -> hits lines 3-7 (return True)
    assert triples_sum_to_zero([1, 2, -3, 4]) is True


def test_triples_sum_to_zero_false():
    # No triple sums to zero -> hits lines 3-6 and 8 (return False)
    assert triples_sum_to_zero([1, 2, 3, 4]) is False


def test_triples_sum_to_zero_empty():
    # Empty list -> loops never run, returns False via line 8
    assert triples_sum_to_zero([]) is False


def test_triples_sum_to_zero_too_short():
    # Fewer than 3 elements -> inner loops never execute, returns False
    assert triples_sum_to_zero([0, 0]) is False
