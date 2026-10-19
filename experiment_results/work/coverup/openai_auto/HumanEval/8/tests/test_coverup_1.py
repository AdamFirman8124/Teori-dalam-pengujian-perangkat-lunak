# file: script_8.py:4-18
# asked: {"lines": [12, 13, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}
# gained: {"lines": [12, 13, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}

from typing import List, Tuple
import pytest
from script_8 import sum_product


def test_sum_product_empty() -> None:
    assert sum_product([]) == (0, 1)


def test_sum_product_nonempty() -> None:
    assert sum_product([1, 2, 3, 4]) == (10, 24)


def test_sum_product_negative() -> None:
    assert sum_product([-1, 5]) == (4, -5)
