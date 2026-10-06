# file: script_60.py:1-14
# asked: {"lines": [14], "branches": []}
# gained: {"lines": [14], "branches": []}

import pytest
from script_60 import sum_to_n


def test_sum_to_n_30():
    assert sum_to_n(30) == 465


def test_sum_to_n_100():
    assert sum_to_n(100) == 5050


def test_sum_to_n_5():
    assert sum_to_n(5) == 15


def test_sum_to_n_10():
    assert sum_to_n(10) == 55


def test_sum_to_n_1():
    assert sum_to_n(1) == 1


def test_sum_to_n_0():
    assert sum_to_n(0) == 0


def test_sum_to_n_negative():
    assert sum_to_n(-5) == 0
