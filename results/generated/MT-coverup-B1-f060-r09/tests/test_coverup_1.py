# file: project/f060/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f060 import sum_to_n


def test_sum_to_n_zero():
    assert sum_to_n(0) == 0


def test_sum_to_n_small_positive():
    assert sum_to_n(1) == 1
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55


def test_sum_to_n_large():
    assert sum_to_n(100) == 5050
    assert sum_to_n(100) == 100 * 101 // 2
