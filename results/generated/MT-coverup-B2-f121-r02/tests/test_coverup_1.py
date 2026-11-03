# file: project/f121/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f121 import solution


def test_solution_sums_odd_values_at_even_indices():
    # idx 0: 1 (even idx, odd value -> included)
    # idx 1: 2 (odd idx -> skipped)
    # idx 2: 3 (even idx, odd value -> included)
    # idx 3: 4 (odd idx -> skipped)
    # idx 4: 5 (even idx, odd value -> included)
    assert solution([1, 2, 3, 4, 5]) == 1 + 3 + 5 == 9


def test_solution_excludes_even_values_at_even_indices():
    # idx 0: 2 (even idx, even value -> excluded)
    # idx 1: 1 (odd idx -> skipped)
    # idx 2: 4 (even idx, even value -> excluded)
    # idx 3: 3 (odd idx -> skipped)
    # idx 4: 6 (even idx, even value -> excluded)
    assert solution([2, 1, 4, 3, 6]) == 0


def test_solution_empty_list():
    assert solution([]) == 0


def test_solution_negative_values():
    # idx 0: -1 (even idx, odd value -> included)
    # idx 1: 2 (odd idx -> skipped)
    # idx 2: -3 (even idx, odd value -> included)
    assert solution([-1, 2, -3]) == -4
