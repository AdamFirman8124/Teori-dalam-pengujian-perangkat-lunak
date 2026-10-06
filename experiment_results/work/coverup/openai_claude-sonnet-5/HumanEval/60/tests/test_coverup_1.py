# file: script_60.py:1-14
# asked: {"lines": [14], "branches": []}
# gained: {"lines": [14], "branches": []}

import pytest
from script_60 import sum_to_n


def test_sum_to_n_thirty():
    assert sum_to_n(30) == 465


def test_sum_to_n_hundred():
    assert sum_to_n(100) == 5050


def test_sum_to_n_five():
    assert sum_to_n(5) == 15


def test_sum_to_n_ten():
    assert sum_to_n(10) == 55


def test_sum_to_n_one():
    assert sum_to_n(1) == 1


def test_sum_to_n_zero():
    assert sum_to_n(0) == 0


def test_sum_to_n_two():
    assert sum_to_n(2) == 3
