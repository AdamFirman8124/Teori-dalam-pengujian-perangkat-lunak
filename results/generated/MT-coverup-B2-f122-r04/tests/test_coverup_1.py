# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f122 import add_elements


def test_add_elements_sums_small_elements_within_k():
    # Line 3 executes: generator sums elements among the first k whose
    # string representation has length <= 2 (1, -2, 18 all qualify).
    assert add_elements([1, -2, 18, 0, 100, 3], 3) == 17  # 1 + (-2) + 18


def test_add_elements_ignores_elements_beyond_k():
    # Slicing branch: 100 and 3 lie beyond k=2, so only 1 and -2 are summed.
    assert add_elements([1, -2, 100, 3], 2) == -1


def test_add_elements_filters_large_elements():
    # Condition branch: 99 (len 2) is included, 100 (len 3) is excluded.
    assert add_elements([99, 100, 5], 3) == 104


def test_add_elements_all_filtered_out():
    # Every element fails the condition, so the sum is 0.
    assert add_elements([100, 200, 300], 3) == 0


def test_add_elements_empty_array():
    assert add_elements([], 4) == 0


def test_add_elements_k_zero():
    # k=0 yields an empty slice, so the sum is 0.
    assert add_elements([1, 2, 3], 0) == 0
