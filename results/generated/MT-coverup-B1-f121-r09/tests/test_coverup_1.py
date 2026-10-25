# file: project/f121/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f121 import solution


def test_empty_list():
    assert solution([]) == 0


def test_single_odd_at_even_index():
    assert solution([1]) == 1


def test_single_even_at_even_index():
    assert solution([2]) == 0


def test_odd_at_odd_index_excluded():
    # idx 1 is odd, so value 1 must be excluded even though it is odd
    assert solution([0, 1]) == 0


def test_even_at_even_index_excluded():
    # idx 0 and 2 are even but values are even, so excluded
    assert solution([2, 1, 4]) == 0


def test_mixed_even_indices_odd_values():
    # idx 0 -> 5 included, idx 1 -> 2 excluded (odd idx), idx 2 -> 7 included,
    # idx 3 -> 4 excluded (odd idx), idx 4 -> 9 included
    assert solution([5, 2, 7, 4, 9]) == 21


def test_all_branches_combined():
    # idx 0 even + odd -> included (1)
    # idx 1 odd + even -> excluded (short-circuit on idx)
    # idx 2 even + even -> excluded (second condition False)
    # idx 3 odd + odd -> excluded (short-circuit on idx)
    assert solution([1, 2, 4, 3]) == 1


def test_negative_odd_numbers():
    # in Python -1 % 2 == 1 and -3 % 2 == 1, so they count as odd
    assert solution([-1, -2, -3]) == -4
