# file: project/f060/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f060 import sum_to_n


def test_sum_to_n_zero():
    assert sum_to_n(0) == 0


def test_sum_to_n_positive():
    assert sum_to_n(5) == 15


def test_sum_to_n_negative():
    assert sum_to_n(-1) == 0
