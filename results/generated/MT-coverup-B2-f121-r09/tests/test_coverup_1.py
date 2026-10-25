# file: project/f121/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f121 import solution


def test_empty_list():
    assert solution([]) == 0


def test_single_odd_at_even_index_included():
    # idx=0 even True, x=1 odd True -> True and True -> included
    assert solution([1]) == 1


def test_single_even_at_even_index_excluded():
    # idx=0 even True, x=2 odd False -> True and False -> excluded
    assert solution([2]) == 0


def test_odd_value_at_odd_index_excluded():
    # idx=1 even False -> short-circuit False, even though x=3 is odd
    assert solution([2, 3]) == 0


def test_even_value_at_odd_index_excluded():
    # idx=0 included, idx=1 even False -> excluded
    assert solution([1, 2]) == 1


def test_mixed_even_indices_odd_values():
    # idx0=5 included, idx1=6 excluded, idx2=7 included, idx3=8 excluded, idx4=9 included
    assert solution([5, 6, 7, 8, 9]) == 21


def test_all_even_values_at_even_indices_excluded():
    assert solution([0, 1, 2, 3, 4]) == 0


def test_negative_odd_values():
    # -1 % 2 == 1 and -3 % 2 == 1 in Python, so both included
    assert solution([-1, -2, -3]) == -4
