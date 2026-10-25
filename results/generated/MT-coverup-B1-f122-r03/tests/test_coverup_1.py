# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f122 import add_elements


def test_add_elements_includes_only_short_elements():
    # Elements whose string length <= 2 are summed; longer ones are skipped.
    assert add_elements([1, -2, 22, 100, 999], 5) == 21  # 1 + (-2) + 22


def test_add_elements_respects_k():
    # Only the first k elements are considered.
    assert add_elements([1, 2, 3, 4, 5], 3) == 6
    assert add_elements([1, 2, 3, 4, 5], 0) == 0


def test_add_elements_empty():
    assert add_elements([], 3) == 0


def test_add_elements_k_exceeds_length():
    # Slicing beyond the list length is safe.
    assert add_elements([10, 20], 10) == 30


def test_add_elements_all_filtered_out():
    # Every element is filtered out by the length condition.
    assert add_elements([111, 222, 333], 3) == 0
